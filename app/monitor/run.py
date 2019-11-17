import sys
sys.path.append('/opt/ring/app/monitor')
import os
import time
import logging
import traceback
from multiprocessing import Process

import const, ring, gdrive
    
def main(ring_service, gdrive_service):
    limit = 5
    history = []
    first_run = True
    while True:
        for doorbell in ring_service.session.doorbells:
            skip = False
            for event in doorbell.history(limit=limit):
                if len(history) == limit and event['id'] in history:
                    continue
                elif event['id'] not in history:
                    if event['kind'] not in ['motion', 'ding']:
                        continue
                    logger.info("%s - %s - %s" % (event['id'], event['kind'], event['created_at']))
                    if len(history) == limit:
                        history.pop(0)
                    history.append(event['id'])
                    if not first_run and not skip:
                        def upload_recording():
                            try:
                                recorded_file = ring_service.save_recording(event)
                                gdrive_service.upload(recorded_file)
                                os.remove(recorded_file)
                            except Exception as e:
                                logger.error(traceback.format_exc())
                                logger.error('Failed to save recording: %s' % str(e))
                        p = Process(target=upload_recording)
                        p.start()
                        skip = True
        first_run = False
        time.sleep(5)


if __name__ == '__main__':
    logging.basicConfig(filename=const.LOG_FILE, filemode='w',
        format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO)
    logger = logging.getLogger('ring')
    ring_service = ring.RingDoorbell(const.RING_EMAIL, const.RING_PASS)
    gdrive_service = None # gdrive.GDrive(const.GDRIVE_CRED_FILE, const.GDRIVE_CLIENT_FILE)
    main(ring_service, gdrive_service)
