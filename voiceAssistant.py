from voiceInput import *
from chatgptProcessing import *
from voiceOutput import *

class VoiceAssistant(object):


    def __init__(self):
        self._up=True
        self._vo=VoiceOutput()
        self._vi=VoiceInput()
        self._speechInput=""
        self._chatgpt=ChatgptProcessing()
        self._vi.get_noise_level()
        
    def run(self):        
        try:
            self._vi.translate()
            text=self._vi.text
            if ("Sarah" in text):
                self._up=True
            if ("tais-toi" in text):
                self._up=False
                self._vo.translate("Ok n'hésitez pas à m'appeler au besoin Monsieur")

            if (self._up):
                self._chatgpt.answer(text)
                self._vo.translate(self._chatgpt.response.content)
        except:
            pass











