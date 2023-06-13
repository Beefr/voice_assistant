from mainModule.voiceInput import *
from mainModule.chatgptProcessing import *
from mainModule.voiceOutput import *
from vision.imageInput import ImageInput
from musique.musique import Musique

class VoiceAssistant(object):


    def __init__(self):
        self._up=True
        self._vo=VoiceOutput()
        self._vi=VoiceInput()
        self._speechInput=""
        self._chatgpt=ChatgptProcessing()
        self._vi.get_noise_level()
        self._ii=ImageInput()
        self._vo.translate("Bonjour Monsieur")
        self._mu=Musique()
      
        
    def run(self):        
        try:
            self._vi.translate()
            text=self._vi.text
            if ("Sarah" in text):
                self._up=True
            if ("tais-toi" in text):
                self._up=False
                self._vo.translate("Ok n'hésitez pas à m'appeler au besoin Monsieur")

            
            if ("regarde" in text):
                self._vo.translate("Je regarde ça tout de suite Monsieur")
                elem=' '.join(self._ii.run())
                results="Voici le contenu de l'image dont je vais te parler: "+elem+"."
                print(results+text)
                self._chatgpt.answer(text+results)
                print("\n\n\n"+elem)
                self._vo.translate(self._chatgpt.response.content)

            elif ("lecteur musique" in text):
                if ("next" in text):
                    self._vo.translate("Lecture de la prochaine musique")
                    self._mu.playNext()
                elif ("previous" in text):
                    self._vo.translate("Lecture de la musique précédente")
                    self._mu.previous()
                elif ("pause" in text):
                    self._mu.pause()
                    self._vo.translate("Mise en pause")
                elif ("stop" in text):
                    self._mu.stop()
                    self._vo.translate("Arrêt de la musique")
                elif ("joue" in text):
                    self._vo.translate("Reprise de la musique")
                    self._mu.play()
                else:
                    #librairie="J'ai toutes ces musiques: "+str(self._mu.library)
                    #self._vo.translate(librairie+text)
                    self._vo.translate("Désolé je n'ai pas compris l'instruction pour le lecteur de musique.")

            elif (self._up):
                self._chatgpt.answer(text)
                self._vo.translate(self._chatgpt.response.content)
        except:
            pass










