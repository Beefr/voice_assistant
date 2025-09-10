#import speech_recognition as sr
#from pocketsphinx import LiveSpeech

from STT.useSTT import *

class VoiceInput(object):

    def __init__(self):
        self._client = STT()
        


    @property
    def text(self):
        return self._client.input_text()
        


    def __del__(self):
        self._client.terminate()


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
    
