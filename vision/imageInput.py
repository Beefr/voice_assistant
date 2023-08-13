#from imageai.Detection import ObjectDetection
import tensorflow as tf
from tensorflow import keras
#import cv2
import os
from vision.videoInput import VideoInput
import numpy as np


from object_detection.utils import visualization_utils as vis_util

class ImageInput(object):

    def __init__(self):
        #self._client = ObjectDetection()          
        self._base_path = os.path.join(os.getcwd(), "voice_assistant/vision/")
        #self._client.setModelTypeAsTinyYOLOv3() 
        print(self._base_path+"models/yolo-tiny.h5")
        #self._client.setModelPath(self._base_path+"models/yolo-tiny.h5") 
        
        self._model = tf.keras.models.load_model(self._base_path+"models/yolo-tiny.h5") 
        #self._client.loadModel()  

        self._video=VideoInput(self._base_path)
        self._video.run()

    @property 
    def video(self):
        return self._video
        
    @video.setter
    def video(self, video):
        self._video=video

    def run(self):
        #vid = cv2.VideoCapture(0)
        #_, frame = vid.read()
        frame=self._video.currentFrame()
        #if not self._video.isOpened():
        #    return ["rien"]
        #cv2.imwrite('{}input\\input.jpg'.format(self._base_path), frame)

        #recognition = self._client.detectObjectsFromImage(  
        #    input_image = self._base_path+"input\\input.jpg",  
        #    output_image_path = self._base_path+"input\\output.jpg"  
        #) 
        output_dict=self.show_inference(self._model, frame)

         
         
        # list of item in the scene
        result=[]
        for eachItem in output_dict['detection_classes']:  
            result.append(eachItem["name"]) 

        #vid.release()
        if result==[]: return ["rien. \n"]
        return result       

    def show_inference(self, model, frame):
        image_np = np.array(frame)
        output_dict = self.run_inference_for_single_image(model, image_np)
 
        return(output_dict)
    
    def run_inference_for_single_image(self, model, img):
        image = np.asarray(image)
        # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
        input_tensor = tf.convert_to_tensor(image)
        # The model expects a batch of images, so add an axis with `tf.newaxis`.
        input_tensor = input_tensor[tf.newaxis,...]
        
        # Run inference
        model_fn = model.signatures['serving_default']
        output_dict = model_fn(input_tensor)
        
        # All outputs are batches tensors.
        # Convert to numpy arrays, and take index [0] to remove the batch dimension.
        # We're only interested in the first num_detections.
        num_detections = int(output_dict.pop('num_detections'))
        output_dict = {key:value[0, :num_detections].numpy() 
                        for key,value in output_dict.items()}
        output_dict['num_detections'] = num_detections
        
        # detection_classes should be ints.
        output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
            
        # Handle models with masks:
        if 'detection_masks' in output_dict:
            # Reframe the the bbox mask to the image size.
            detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                    output_dict['detection_masks'], output_dict['detection_boxes'],
                    image.shape[0], image.shape[1])      
            detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5,
                                            tf.uint8)
            output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()
            
        return output_dict
