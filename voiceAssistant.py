from voiceInput import *
from chatgptProcessing import *
from voiceOutput import *
#import threading
#import time

class VoiceAssistant(object):


    def __init__(self):
        self._up=True
        self._vo=VoiceOutput()
        self._vi=VoiceInput()
        self._speechInput=""
        self._chatgpt=ChatgptProcessing()
        
    def run(self):
        self._vi.get_noise_level()
        while True:
            print(self._up)
            try:
                self._vi.translate()
                text=self._vi.text
                if ("Sarah" in text):
                    self._up=True
                if ("tais-toi" in text):
                    self._up=False

                print(text+"\n")

                if (self._up):
                    self._chatgpt.answer(text)
                    print(self._chatgpt.response)
                    self._vo.translate(self._chatgpt.response.content)
            except:
                self._vo.translate("Désolé, je n'ai pas compris")
        self.run()


"""     def is_done_speaking_event(self, doneSpeaking):
        self._vi.translate()
        while not doneSpeaking.is_set():
            self._speechInput=self._vi.text
            VoiceAssistant.is_he_done_speaking(doneSpeaking, self._speechInput)
            time.sleep(1)
        
        if ("Sarah" in self._speechInput):
            self._up=True
        if ("tais-toi" in self._speechInput):
            self._up=False

        print("\nSpeech detected: "+self._speechInput+"\n")
        print("Allowed to talk:"+self._up)
        if (self._up):
            self._vo.translate(self._speechInput)


    @staticmethod
    def is_he_done_speaking(doneSpeaking, text):
        print("Listening: "+text)
        if (text==""):
            pass
        else:
            doneSpeaking.set()




    def is_done_answering_event(self, doneSpeaking, doneAnswering):
        while not doneAnswering.is_set():
            if doneSpeaking.is_set():
                self._vo.translate(self._speechInput)
                VoiceAssistant.is_he_done_answering(doneAnswering, self._vo.done)
            if doneAnswering.is_set():
                self._vo.done=False


    @staticmethod
    def is_he_done_answering(doneAnswering, done):
        print("Answering")
        if (done):
            doneAnswering.set()



    def run2(self):
        doneSpeaking= threading.Event()
        doneAnswering= threading.Event()

        # thread to listen to speakers
        t1 = threading.Thread(name='doneSpeaking', 
                              target=self.is_done_speaking_event,
                              args=(doneSpeaking, ))
        t1.start()

        # thread to answer
        t2 = threading.Thread(name='doneAnswering', 
                              target=self.is_done_answering_event,
                              args=(doneSpeaking, doneAnswering, ))
        t2.start()
 """













