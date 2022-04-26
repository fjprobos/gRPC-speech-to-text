# Imports the Google Cloud client library
from google.cloud import speech
import io
import pyaudio
import wave
from google.cloud import speech_v1p1beta1
import grpc

#
#
# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "voice.wav"
#
# p = pyaudio.PyAudio()
#
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)
#
# print("* recording")
#
# frames = []
#
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
#
# print("* done recording")
#
# stream.stop_stream()
# stream.close()
# p.terminate()
#
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()
#





# Tries to create a transport
#channel = grpc.insecure_channel('localhost:8080')
#transport = speech.services.speech.transports.SpeechGrpcTransport(
#    channel=channel
#)

# Instantiates a client
#client = speech_v1p1beta1.SpeechClient(transport=transport)
client = speech.SpeechClient()

# The name of the audio file to transcribe
#gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
with io.open("voice.wav", "rb") as audio_file:
    content = audio_file.read()

#audio = {"content": content}
#audio = speech.RecognitionAudio(uri=gcs_uri)

# In practice, stream should be a generator yielding chunks of audio data.
stream = [content]

requests = (
    speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
)


config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
    enable_word_time_offsets=True,
)

streaming_config = speech.StreamingRecognitionConfig(config=config)

# streaming_recognize returns a generator.
responses = client.streaming_recognize(
    config=streaming_config,
    requests=requests,
)

for response in responses:
    # Once the transcription has settled, the first result will contain the
    # is_final result. The other results will be for subsequent portions of
    # the audio.
    for result in response.results:
        print("Finished: {}".format(result.is_final))
        print("Stability: {}".format(result.stability))
        alternatives = result.alternatives
        # The alternatives are ordered from most likely to least.
        for alternative in alternatives:
            print("Confidence: {}".format(alternative.confidence))
            print(u"Transcript: {}".format(alternative.transcript))

# response = client.recognize(request={"config": config, "audio": audio})
# for result in response.results:
#     # First alternative is the most probable result
#     alternative = result.alternatives[0]
#     print(f"Transcript: {alternative.transcript}")
