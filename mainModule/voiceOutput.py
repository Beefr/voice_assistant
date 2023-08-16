import pyttsx3

class VoiceOutput(object):

    def __init__(self):
        self._engine= pyttsx3.init()
        self._engine.setProperty('voice', 'french')
        self._engine.setProperty('rate',105)
        self._engine.setProperty('pitch', 0.8)

    def translate(self, text):
        self._engine.say(text)
        self._engine.runAndWait()
        return
