# Ring Doorbell using Google Drive storage

This project is made possible by:
* [ring-client-api](https://github.com/dgreif/ring): for saving recordings 
* [python-ring-doorbell](https://github.com/tchellomello/python-ring-doorbell): for listening for events


### Requirements

* [Docker](https://www.docker.com/products/docker-desktop)
* Google Drive Account Setup
    * Enable the Drive API and download the [credentials.json](https://developers.google.com/drive/api/v3/quickstart/python)
        * Add the file to ```app/monitor/credentials.json```
    * Create the OAuth client ID and download the [client_secret.json](https://developers.google.com/drive/api/v3/enable-drive-api)
        * Add the file to ```app/monitor/client_secret.json```
* Ring
    * Create a ```credentials.env``` file with the following variables:
      * ```bash 
        RING_EMAIL=<email>
        RING_PASS=<password>
        GDRIVE_FOLDER_ID=<folder_id>
        ```
        * ```GDRIVE_FOLDER_ID``` (optional) the ID of the folder on Google Drive where the files will be uploaded to. To get the ID, go to Google Drive on the browser, select the folder where the recordings will be uploaded to, and copy the last part of the URL.
          * i.e. 3rE4Hg5vnPfOSZgjq9IrFGk6FWjrJs4Lf 
      * Add the file to ```./```

### Build
```bash
docker build -t ring-gdrive .
```

### Deploy
```bash
docker run --env-file credentials.env -it ring-gdrive
```

This will start an interactive terminal. A Google Sign In link will appear. Copy and paste the link on a browser to sign in with your Google account. After allowing the necessary permissions, copy and paste the verification code into the terminal and press enter.

Now exit the terminal by holding down the  ```ctrl``` key and pressing the ```p``` + ```q``` keys.