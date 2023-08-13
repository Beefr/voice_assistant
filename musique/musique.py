import os
from random import randint
import pygame 

class Musique(object):


    def __init__(self):
        self._musiqueFolder=os.getcwd()+"/voice_assistant/musique/library"
        self.getLibrary()
        self.listGroups()
        self._historique=[]
        self._groupeHistorique=[]
        self._mixer=pygame.mixer.init()
        self._index=-1
        pygame.mixer.music.set_volume(0.05)

    @property
    def library(self):
        return self._library

    def getLibrary(self): 
        self._library={}
        for directory in os.listdir(self._musiqueFolder): 
            musique=os.listdir(self._musiqueFolder+"/"+directory)
            files = [os.path.splitext(filename)[0] for filename in musique]
            self._library[directory]=files
        

    def next(self):
        length=len(self._listGroups)
        groupe=self._listGroups[randint(0,length-1)]
        folderContent=os.listdir(self._musiqueFolder+"/"+groupe)
        val=randint(0,len(folderContent)-1)
        self._historique.append(folderContent[val])
        self._groupeHistorique.append(groupe)
    
    def listGroups(self):
        self._listGroups=list(self._library.keys())

    def playNext(self):
        self.next()
        self._index+=1
        groupe=self._groupeHistorique[self._index]
        song=self._historique[self._index]
        pygame.mixer.music.load(self._musiqueFolder+"/"+groupe+"/"+song)
        self.play()

    def play(self):
        pygame.mixer.music.play()
        if pygame.mixer.music.get_endevent():
            self.playNext

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def resume(self):
        pygame.mixer.music.unpause()


    def previous(self):
        if (self._index==0):
            return
        self._index-=1
        groupe=self._groupeHistorique[self._index]
        previousMusic=self._historique[self._index]
        pygame.mixer.music.load(self._musiqueFolder+"/"+groupe+"/"+previousMusic)
        self.play()

