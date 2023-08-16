from gtts import gTTS
import os

class VoiceOutput(object):

    def __init__(self):
        try:
            os.remove('output.mp3')
        except:
            pass


    def translate(self, text):
        speech = gTTS(text, lang='fr')
        speech.save('./output.mp3')
        os.system('mpg123 -q ./output.mp3')
        os.remove('./output.mp3')
        return
