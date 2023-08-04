

import cv2
import threading

from datetime import datetime


def VideoInput(object):

    def __init__(self, basePath):
        self._framerate=20 # images / seconde
        self._delay=1/self._framerate # interval between each capture

        self._backup=10 # secondes
        self._queueLength=self._backup*self._framerate # number of frames keeped

        self._basePath=basePath
        self._start=False
        self._queue=[]
        self._vid = cv2.VideoCapture(0)

        frame_width = int(self._vid.get(3))
        frame_height = int(self._vid.get(4))
        self._size = (frame_width, frame_height)


        self._timer= threading.Timer(self._delay, self.run)



    def run(self):
        if not self._vid.isOpened():
            return None
        _, frame = self._vid.read()
        self._queue.append(frame)

        if self._start:
            pass # we keep saving frames for the video we want to save
        elif len(self._queue)>=self._queueLength:
            while len(self._queue)>=self._queueLength:
                self._queue.pop(0)
                # we release frames since we are done filming
        
        self._timer= threading.Timer(self._delay, self.run)
        self._timer.start()


    def __del__(self):
        self._vid.release()


    def start(self):
        if self._start:
            pass
        else:
            self._start=True
    
    def stop(self):
        self._start=False
        self.stopEnregistrement()

    

    def stopEnregistrement(self):
        result = cv2.VideoWriter('filename_{}.avi'.format(datetime.now().strftime("%d/%m/%Y_%H:%M:%S")),  cv2.VideoWriter_fourcc(*'mp4v'), 10, self._size)
        for frame in self._queue:
            result.write(frame)
        result.release()
        # enregistrement des frames en une video