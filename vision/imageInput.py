from imageai.Detection import ObjectDetection
import cv2
import os

class ImageInput(object):

    def __init__(self):
        self._client = ObjectDetection()  
        self._base_path = os.path.join(os.getcwd(), "vision")
        self._client.setModelTypeAsTinyYOLOv3()  
        self._client.setModelPath(self._base_path+"\models\yolo-tiny.h5") 
        self._client.loadModel()  
        
        

    def run(self):
        vid = cv2.VideoCapture(0)
        _, frame = vid.read()
        if not vid.isOpened():
            return ["rien"]
        cv2.imwrite('{}input.jpg'.format(self._base_path), frame)

        recognition = self._client.detectObjectsFromImage(  
            input_image = self._base_path+"\input\input.jpg",  
            output_image_path = self._base_path+"\input\output.jpg"  
        )  
        # list of item in the scene
        result=[]
        for eachItem in recognition:  
            result.append(eachItem["name"]) 

        vid.release()
        if result==[]: return ["rien. \n"]
        return result       