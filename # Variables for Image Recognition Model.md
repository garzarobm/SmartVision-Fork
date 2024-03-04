# Variables for Image Recognition Model

## Independent Variables

1. **Dataset Size**: The number of images in the dataset. This can be 10,250, 5,200, or 100-200.
2. **Image Resolution**: The quality of the images in the dataset.
3. **Image Color**: Whether the images are grayscale or colored.
4. **Image Angle**: The actual angle of the image, i.e., what 3 the image is depicting.
5. **Image Format**: The format of the image files (JPEG, PNG, etc.).
6. **Image Orientation**: Whether the image is portrait or landscape.
7. **light brightness**: supporting lights will maintain the same position and only change in the overall lumen count. 

## Dependent Variables

1. **Model Accuracy**: The accuracy of the image recognition model in correctly identifying the content of the images.
2. **Model Precision**: The precision of the model in correctly identifying the content of the images.
3. **Model Recall**: The recall of the model in correctly identifying the content of the images.
4. **Model F1 Score**: The F1 score of the model in correctly identifying the content of the images.

## Control Variables

1. **Image Content**: The actual content of the image, i.e., what the image is depicting.
2. **Origin and 3-D face of object**: the actual placement of the origin and the corresponding faces top front back bottom in left/right faces) 
3. **Origin Position of 3d Object** object will maintain origin and only translate in the Y axis, while photos are being taken. 
4. **Hardware (Camera, computer/microprocessor) running model**: in order to control the environment and ensure as little change as possible between independent variables, all models will run the raspberry pie attached with a Google corral device via USB

## Models for classifications

#### For implementing basic image recognition on a Raspberry Pi with a Google Coral for the purpose of object detection, particularly household item recognition, several algorithms can be utilized. These algorithms fall into two main categories: traditional object detection algorithms and deep learning-based object detection algorithms. 

Traditional Object Detection Algorithms (Before 2014)
1. Viola-Jones Detector (2001): Pioneering work that started the development of traditional object detection methods.
2. HOG Detector (2006): A popular feature descriptor for object detection in computer vision and image processing.
3. DPM (2008): Introduced the first use of bounding box regression.
Two-Stage Object Detection Algorithms
1. RCNN and SPPNet (2014): Introduced the concept of using regions with CNN features.Fast RCNN and Faster RCNN (2015): Improved speed and accuracy by sharing computations and using a region proposal network.
2. Mask R-CNN (2017): Extended Faster RCNN for pixel-level segmentation.
3. Pyramid Networks/FPN (2017): Utilized a top-down architecture with lateral connections for building high-level semantic feature maps at all scales.
4. G-RCNN (2021): A more recent development in two-stage object detection.

One-Stage Object Detection Algorithms

YOLO (You Only Look Once) series (2016-2023): A family of algorithms (YOLO, YOLOv3, YOLOv4, YOLOR, YOLOv7, YOLOv8) known for their speed and efficiency, making them suitable for real-time object detection.
1. SSD (Single Shot MultiBox Detector) (2016): Uses a single deep neural network to detect multiple objects within the image.
2. RetinaNet (2017): Introduced the focal loss function to address class imbalance during training.

1. Deep CNN
2. RNN
3. SSD
4. [Missing Model]

## Datasets
(at LEAST 3 Difference sized datasets of the same items)
1. **Dataset 1**: Contains 10,250 images.
2. **Dataset 2**: Contains 5,200 images.
3. **Dataset 3**: Contains between 100 and 200 images.

------------------

<!-- ## Limitations:
Using object detection algorithms on a Raspberry Pi with a Google Coral has several limitations:



### Hardware Limitations
- **Compute Resources:** The Raspberry Pi has limited computational resources, which can make video object recognition tasks challenging without additional hardware like the Google Coral AI Edge TPU[2][7].
- **Memory Constraints:** The Raspberry Pi often comes with limited RAM (e.g., 1GB for earlier models), which can be a bottleneck for running complex deep learning models[3].
- **USB Interface:** The Raspberry Pi 3 B+ has a USB 2.0 interface, which can limit the data transfer speed to the Google Coral, potentially affecting performance. Newer models like the Raspberry Pi 4 have USB 3.0 interfaces, which are faster and more suitable for high-speed data transfer[3].

### Software and Model Limitations
- **Model Compatibility [model list link](https://qengineering.eu/deep-learning-with-raspberry-pi-and-alternatives.html):** The Google Coral works with special pre-compiled TensorFlow Lite networks. If the topology of the neural network and its required operations can be described in TensorFlow Lite, it may work well on the Coral. However, not all models are compatible with the Coral's TPU[3].
- **Training Limitations:** The Google Coral TPU is designed for inference, not for training models. Only the last layer of a network can be slightly modified on the device, meaning that you can only import and run an already trained model[3].
- **Preprocessing Requirements:** Models need to be converted from floating-point to quantized formats (e.g., from floats to bytes) to be compatible with the TPU, which can be a complex process[3].

### Performance Limitations
- **Inference Speed:** While the Google Coral TPU accelerates inference, the speed at which the system calculates the tensors from the image detection model can still be limited by the Raspberry Pi's processing capabilities[5].
- **Heat Management:** Continuous operation of the Raspberry Pi and the Google Coral TPU can generate significant heat, which may require additional cooling solutions to prevent overheating[4].

### Practical Limitations
- **Real-time Processing:** Applications that require real-time calculations, such as video object recognition, are computationally intensive. The Google Coral USB Accelerator helps with this, but there may still be limitations in terms of the refresh rate of the video stream and the control system[5].
- **Software Dependencies:** The use of specific libraries and tools is necessary to benefit from the Coral USB Accelerator's capabilities, which can add complexity to the setup process[4].

In summary, while the Google Coral AI Edge TPU can significantly enhance the Raspberry Pi's capabilities for object detection tasks, there are limitations related to hardware resources, model compatibility, training capabilities, inference speed, heat management, real-time processing requirements, and software dependencies[1][2][3][4][5][7].~~

Citations:
[1] https://circuitdigest.com/news/raspberry-pi-pushed-to-its-limits-with-coral-ai-edge-tpu-for-video-object-recognition
[2] https://www.toolify.ai/ai-news/supercharge-your-raspberry-pi-with-googles-coral-ai-edge-tpu-2624542
[3] https://qengineering.eu/deep-learning-with-raspberry-pi-and-alternatives.html
[4] https://tutorials-raspberrypi.com/using-tensorflow-lite-with-google-coral-tpu-on-raspberry-pi-4/
[5] https://www.diva-portal.org/smash/get/diva2:1708300/FULLTEXT01.pdf
[6] https://pyimagesearch.com/2019/05/13/object-detection-and-image-classification-with-google-coral-usb-accelerator/
[7] https://www.toolify.ai/ai-news/unlocking-the-power-of-raspberry-pi-with-coral-ai-a-supercomputer-for-video-object-recognition-2622287
[8] https://www.sciencedirect.com/science/article/pii/S0167926023001694 -->
[TODO: check citations and texts and make changes before pushing to master] 