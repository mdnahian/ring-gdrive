import os
import logging

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload

logger = logging.getLogger('ring')

class GDrive:
    def __init__(self, credentials_file, client_file):
        SCOPES = 'https://www.googleapis.com/auth/drive.file'
        store = file.Storage(credentials_file)
        creds = None
        try:
            creds = store.get()
        except:
            pass
        if not creds or creds.invalid:
            args = tools.argparser.parse_args()
            args.noauth_local_webserver = True
            flow = client.flow_from_clientsecrets(client_file, SCOPES)
            creds = tools.run_flow(flow, store, args)
        self.service = build('drive', 'v3', http=creds.authorize(Http()))
        logger.info("Connected to Google Drive account")

    def upload(self, file, folder=None):
        file_name = os.path.basename(file)
        file_metadata = {
            'name': file_name,
            'mimeType': '*/*'
        }
        if folder is not None:
            file_metadata['parents'] = [folder]
        media = MediaFileUpload(file, mimetype='*/*', resumable=True)
        saved_file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        logger.info('Uploaded file to Google Drive: %s' % saved_file.get('id'))

