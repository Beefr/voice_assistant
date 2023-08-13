import speech_recognition as sr

class VoiceInput(object):

    def __init__(self):
        self._client=sr.Recognizer()
        self._micro=sr.Microphone()
        self._text=""


    @property
    def text(self):
        text=str(self._text)
        self._text=""
        return text

    def get_noise_level(self):
        with self._micro as source:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            self._client.adjust_for_ambient_noise(source, duration=1)
        
    def translate(self):
        #try:
        with self._micro as source:
            #listens for the user's input
            speech = self._client.listen(source, phrase_time_limit = 5)
                
        # Using google to recognize audio
        self._text=self._client.recognize_google(speech, language="fr-FR")
    