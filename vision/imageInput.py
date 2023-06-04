from imageai.Detection import ObjectDetection
import cv2
import os

class ImageInput(object):

    def __init__(self):
        self._client = ObjectDetection()  
        path_model = "./vision/models/yolo-tiny.h5"  
        self._path_input = "./vision/input/images.jpg"  
        self._path_output = "./vision/output/newimage.jpg"
        self._client.setModelTypeAsTinyYOLOv3()  
        self._client.setModelPath(path_model) 
        self._client.loadModel()  
        
        

    def run(self):
        vid = cv2.VideoCapture(0)
        _, frame = vid.read()
        if not vid.isOpened():
            return ["rien"]
        base_path = os.path.join(os.getcwd(), "vision\input\images")
        print(base_path)
        cv2.imwrite('{}.jpg'.format(base_path), frame)

        recognition = self._client.detectObjectsFromImage(  
            input_image = self._path_input,  
            output_image_path = self._path_output  
        )  
        # list of item in the scene
        result=[]
        for eachItem in recognition:  
            result.append(eachItem["name"]) 

        vid.release()
        if result==[]: return ["rien. \n"]
        return result       