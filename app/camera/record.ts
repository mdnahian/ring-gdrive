import { RingApi } from 'ring-client-api'

async function saveRecording(outputFile) {
  const ringApi = new RingApi({
      email: process.env.RING_EMAIL!,
      password: process.env.RING_PASS!,
      debug: true
    }),
    [camera] = await ringApi.getCameras()

  if (!camera) {
    console.log('No cameras found')
    return
  }
  await camera.recordToFile(outputFile, 10)
  process.exit(0)
}

var args = process.argv.slice(2);
var outputFile = args[0]
saveRecording(outputFile)