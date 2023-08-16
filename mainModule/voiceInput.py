import speech_recognition as sr
from pocketsphinx import LiveSpeech


class VoiceInput(object):

    def __init__(self):
        self._client = LiveSpeech(
                #lm='fr_FR/fr-small.lm.bin',
                #dic='fr_FR/fr.dic',
                kws_threshold=1e-20,
                sampling_rate=48000,
                buffer_size=2048)
        #self._client=sr.Recognizer()
        #self._micro=sr.Microphone()
        self._text=""
        for phrase in self._client:
            print(phrase)
            self._text=phrase


    @property
    def text(self):
        text=str(self._text)
        self._text=""
        return text


    def __del__(self):
        self._engine.stop


    def get_noise_level(self):
        return
        #with self._micro as source:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
         #   self._client.adjust_for_ambient_noise(source, duration=1)
        
    def translate(self):
        pass
        #with self._micro as source:
            #listens for the user's input
            #speech = self._client.listen(source, phrase_time_limit = 5)
                
        # Using google to recognize audio
        #self._text=self._client.recognize_google(speech, language="fr-FR")
        #for phrase in self._client:
         #   print(phrase)
          #  self._text=phrase
    
