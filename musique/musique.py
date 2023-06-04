import os
from random import randint
import pygame 

class Musique(object):


    def __init__(self):
        self._musiqueFolder=os.getcwd()+"\\musique\\library"
        self.getLibrary()
        #self.listSongs()
        self.listGroups()
        #print(self._library)
        self._historique={}
        self._mixer=pygame.mixer.init()
        self.next()
        self._index=0
        
        pygame.mixer.music.load(self._musiqueFolder+"\\"+self._group+"\\"+self._song)

    @property
    def library(self):
        return self._library

    def getLibrary(self): 
        self._library={}
        for directory in os.listdir(self._musiqueFolder): 
            musique=os.listdir(self._musiqueFolder+"\\"+directory)
            self._library[directory]=musique
        

    def next(self):
        length=len(self._listGroups)
        self._group=self._listGroups[randint(0,length-1)]
        folderContent=os.listdir(self._musiqueFolder+"\\"+self._group)
        val=randint(0,len(folderContent)-1)
        self._historique[folderContent[val]]=0
        self._song=folderContent[val]
    
    def listGroups(self):
        self._listGroups=list(self._library.keys())

    """ 
        def listSongs(self):
        self._liste=[]
        musics=list(self._library.values())
        for groupe in musics:
            for musique in groupe:
                self._liste.append(musique) 
    """
        

    def playNext(self):
        print(self._index+1)
        print(len(self._historique))
        if (self._index+1==len(self._historique)):
            pygame.mixer.music.load(self._musiqueFolder+"\\"+self._group+"\\"+self._song)
            self._historique[self._song]= 1
        else:
            nextMusic=list(self._historique.keys())[self._index+1]
            pygame.mixer.music.load(self._musiqueFolder+"\\"+self._group+"\\"+nextMusic)
            self._historique[nextMusic]=1
        self._historique[self._song]=0
        self._song=nextMusic
        self._index+=1
        print(self._song)
        print(self._historique)
        self.play()

    def play(self):
        pygame.mixer.music.play(self._song)
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
        previousMusic=list(self._historique.keys())[self._index-1]
        self._song=pygame.mixer.music.load(self._musiqueFolder+previousMusic)
        self._historique[previousMusic]=1
        self._historique[self._song]=0
        self._song=previousMusic
        self._index-=1
        self.play()

