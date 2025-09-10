from mainModule.voiceInput import *
from mainModule.chatgptProcessing import *
from mainModule.voiceOutput import *
from vision.imageInput import ImageInput
from musique.musique import Musique


import threading

class VoiceAssistant(object):


    def __init__(self, camera, soundInput, soundOutput, chatGPT):
        self._camera=camera
        self._soundInput=soundInput
        self._soundOutput=soundOutput
        self._gpt=chatGPT
        self._up=True

        if self._soundInput:
            self._vi=VoiceInput()
            self._speechInput=""
            self._vi.get_noise_level()

        if self._camera:
            self._ii=ImageInput()

        if soundOutput:
            if self._gpt:
                self._chatgpt=ChatgptProcessing()
            self._vo=VoiceOutput()
            self._mu=Musique()
      
        
        self.talk("Bonjour Monsieur")
        self._timer= threading.Timer(10, self.run)

    def talk(self, msg):
        if self._soundOutput:
            self._vo.translate(msg)
        else:
            print(msg)
        
    def run(self):        
        try:
            self._vi.translate()
            text=self._vi.text
            if ("Sarah" in text):
                self._up=True
            if ("tais-toi" in text):
                self._up=False
                self.talk("Ok n'hésitez pas à m'appeler au besoin Monsieur")

            
            if ("regarde" in text and self._camera):
                self.talk("Je regarde ça tout de suite Monsieur")
                elem=' '.join(self._ii.run())
                results="Voici le contenu de l'image dont je vais te parler: "+elem+"."
                print(results+text)
                if self._gpt:
                    self._chatgpt.answer(text+results)
                    self.talk(self._chatgpt.response.content)
                else:
                    self.talk(elem)
                print("\n\n\n"+elem)

            elif ("vidéo" in text and self._camera):
                if ("début" in text):
                    self.talk("Enregistrement en cours")
                    self._ii.video.start()
                elif ("arrêt" in text):
                    self._ii.video.stop()
                    self.talk("Enregistrement arrêté")

            elif ("lecteur musique" in text and self._soundOutput):
                if ("next" in text):
                    self.talk("Lecture de la prochaine musique")
                    self._mu.playNext()
                elif ("previous" in text):
                    self.talk("Lecture de la musique précédente")
                    self._mu.previous()
                elif ("pause" in text):
                    self._mu.pause()
                    self.talk("Mise en pause")
                elif ("stop" in text):
                    self._mu.stop()
                    self.talk("Arrêt de la musique")
                elif ("joue" in text):
                    self.talk("Reprise de la musique")
                    self._mu.play()
                else:
                    #librairie="J'ai toutes ces musiques: "+str(self._mu.library)
                    #self._vo.translate(librairie+text)
                    self.talk("Désolé je n'ai pas compris l'instruction pour le lecteur de musique.")

            elif (self._up and self._soundOutput and self._gpt):
                self._chatgpt.answer(text)
                self.talk(self._chatgpt.response.content)
        except Exception as error:
            print(error)
        self._timer= threading.Timer(10, self.run) # 10sec comme le temps d'attente de la voix
        self._timer.start()




    def __del__(self):
        try:
            self._timer.cancel()
        except:
            pass


    def currentFrame(self):
        if self._camera:
            return self._ii.video.currentFrame()
        else:
            return None



