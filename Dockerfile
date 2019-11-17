FROM centos:7

RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install python36 python36-devel python36-setuptools && \
    easy_install-3.6 pip && \
    rpm -v --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro && \
    rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm && \
    yum -y install ffmpeg ffmpeg-devel && \
    curl -sL https://rpm.nodesource.com/setup_12.x | bash - && \
    yum -y install nodejs-12.12.0 && \
    mkdir -p /opt/ring/app/camera && \
    mkdir -p /opt/ring/app/monitor && \
    mkdir -p /opt/ring/log && \
    mkdir -p /opt/ring/run/tmp

ADD app/camera /opt/ring/app/camera

RUN cd /opt/ring/app/camera && \
    npm install -g typescript && \
    npm install && \
    npm run build

ADD app/monitor /opt/ring/app/monitor

RUN cd /opt/ring/app/monitor && \
    pip3 install -r requirements.txt

CMD ["python3", "/opt/ring/app/monitor/run.py"]