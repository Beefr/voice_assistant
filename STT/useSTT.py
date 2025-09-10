


from vosk import Model, KaldiRecognizer
import pyaudio
import json
import os


class STT(object):

    def __init__(self):
        self._path = "STT/models/vosk-model-small-en-us-0.15"
        if not os.path.exists(self._path):
            print("STT model path not available, wget the vosk model")
        self._model = Model(self._path)
        self._rec = KaldiRecognizer(self._model, 16000)

        self._p = pyaudio.PyAudio()
        self._streams = self._p.open(format=pyaudio.paInt16, channels =1, rate=16000, input=True, frames_per_buffer=8000)
        self._streams.start_stream()

        self._text = ""

    
        while True:
            data = self._streams.read(4000, exception_on_overflow=False)
            if self._rec.AcceptWaveform(data):
                result = self._rec.Result()
                text = json.loads(result).get("text", "")
            else:
                result = self._rec.PartialResult()
                text= json.loads(result).get("partial", "")
            if text:
                self._text = self._text +  " " + text
            
    def input_text(self):
        text = self._text
        self._text = ""
        return text



    def terminate(self):
        self._streams.stop_stream()
        self._streams.close()
        self._p.terminate()












