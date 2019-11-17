import { RingApi } from 'ring-client-api'

async function saveRecording(outputFile:string) {
  const { env } = process,
  ringApi = new RingApi({
      email: env.RING_EMAIL!,
      password: env.RING_PASS!,
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