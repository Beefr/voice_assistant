from gtts import gTTS
from playsound import playsound
from os import remove

class VoiceOutput(object):

    def __init__(self):
        try:
            remove('output.mp3')
        except:
            pass


    def translate(self, text):
        speech = gTTS(text, lang='fr')
        speech.save('/home/coren/voice_assistant/output.mp3')
        playsound('/home/coren/voice_assistant/output.mp3')
        remove('/home/coren/voice_assistant/output.mp3')
        return