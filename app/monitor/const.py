import os

LOG_DIR = "/opt/ring/log"
LOG_FILE = "%s/ring.log" % LOG_DIR

RUN_DIR = "/opt/ring/run"
RUN_TMP_DIR = "%s/tmp" % RUN_DIR

APP_DIR = "/opt/ring/app"

MONITOR_DIR = "%s/monitor" % APP_DIR
CAMERA_DIR = "%s/camera" % APP_DIR

RING_EMAIL = os.environ.get('RING_EMAIL', None),
RING_PASS = os.environ.get('RING_PASS', None),

GDRIVE_CRED_FILE = '%s/credentials.json' % MONITOR_DIR
GDRIVE_CLIENT_FILE = '%s/client_secret.json' % MONITOR_DIR
GDRIVE_FOLDER_ID = os.environ.get('GDRIVE_FOLDER_ID', None)

RING_ACTION_DIR = "%s/dist" % CAMERA_DIR
RING_RECORD_CMD = "%s/record.js" % RING_ACTION_DIR