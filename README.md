# Ring Doorbell using Google Drive storage


## Build
```bash
docker build -t ring-gdrive .
```

## Deploy
```bash
docker run --env-file credentials.env -d ring-gdrive
```