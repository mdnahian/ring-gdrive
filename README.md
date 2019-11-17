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
        ```
      * Add the file to ```./```

### Build
```bash
docker build -t ring-gdrive .
```

### Deploy
```bash
docker run --env-file credentials.env -d ring-gdrive
```