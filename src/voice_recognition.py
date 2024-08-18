from vosk import Model, KaldiRecognizer
import pyaudio

def recognize_speech():
    model = Model("/home/pi/Course_MOSS/vosk_model/vosk-model-small-cn-0.22")
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("请说话...")

    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = eval(result)['text']
            print(f"你说的是: {text}")
            return text

recognize_speech()
