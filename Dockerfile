FROM jrottenberg/ffmpeg:4.2-centos

# update
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install less && \
    yum -y install tmux 

# create project directories
RUN mkdir -p /opt/ring/app/lib && \
    mkdir -p /opt/ring/app/camera && \
    mkdir -p /opt/ring/app/monitor && \
    mkdir -p /opt/ring/log && \
    mkdir -p /opt/ring/run/tmp
    
# install python and pip
RUN yum -y install python36 python36-devel python36-setuptools && \
    easy_install-3.6 pip && \
    pip3 install supervisor
    
# install nodejs
RUN curl -sL https://rpm.nodesource.com/setup_12.x | bash - && \
    yum -y install nodejs-12.12.0

# add camera project
ADD app/camera /opt/ring/app/camera

# install camera project dependencies
RUN cd /opt/ring/app/camera && \
    npm install -g typescript && \
    npm install && \
    npm run build

# add monitor project
ADD app/monitor /opt/ring/app/monitor

# install monitor project dependencies
RUN cd /opt/ring/app/monitor && \
    pip3 install -r requirements.txt

# add start script
ADD app/start.sh /opt/ring/run
RUN chmod +x /opt/ring/run/start.sh

# add supervisord config
ADD app/supervisord.conf /opt/ring/run

ENTRYPOINT ["supervisord", "-c", "/opt/ring/run/supervisord.conf"]