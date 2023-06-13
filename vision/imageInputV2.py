import cv2
import os
from google.cloud import vision

class ImageInput(object):

    def __init__(self):
        self._client = vision.ImageAnnotatorClient()
        self._path_input = "./vision/input/images.jpg" 
        

    def run(self):
        vid = cv2.VideoCapture(0)
        _, frame = vid.read()
        if not vid.isOpened():
            return ["rien"]
        base_path = os.path.join(os.getcwd(), "vision\input\images")
        print(base_path)
        cv2.imwrite('{}.jpg'.format(base_path), frame)

         
        with open(self._path_input, 'rb') as image_file:
            content = image_file.read()
        self._image = vision.Image(content=content)

        objects = self._client.object_localization(image=self._image).localized_object_annotations

        # list of item in the scene
        result=[]
        for object_ in objects:
            result.append(object_.name) 

        vid.release()
        if result==[]: return ["rien. \n"]
        return result       