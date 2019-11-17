import logging
import subprocess
from ring_doorbell import Ring

import const

logger = logging.getLogger('ring')

class RingDoorbell:
    def __init__(self, username, password):
        self.session = Ring(username, password)
        logger.info("Connected to Ring account: %s" % username)

    def save_recording(self, event):
        output_file = "%s/%s_%s_(%s).mp4" % (const.RUN_TMP_DIR, event['id'], event['kind'], 
            str(event['created_at']).replace(":", "-").replace(" ", "_"))
        subprocess.run(['node', const.RING_RECORD_CMD, output_file])
        logger.info("Saved recording: %s" % output_file)
        return output_file
