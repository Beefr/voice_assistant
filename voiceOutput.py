from gtts import gTTS
from playsound import playsound
from os import remove
#import sys

class VoiceOutput(object):

    def __init__(self):
        #self._done=False
        try:
            remove('output.mp3')
        except:
            pass
            #print('No remnant audio file found')

    #@property
    #def done(self):
    #    return self._done

    #@done.setter
    #def done(self, boolean):
    #    self._done=boolean

    def translate(self, text):
        #try:
        speech = gTTS(text, lang='fr')
        speech.save('output.mp3')
        playsound('output.mp3')
        remove('output.mp3')
        #except:
            #print("Voice output:", sys.exc_info()[0])
        #self._done=True
        return