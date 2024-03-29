# -*- coding: utf-8 -*-
"""Neural Style Transfer with OpenCV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/101y0r8UVZYSwvI2vJoxDMKDGu_D1UXxf
"""

# import the necessary packages
import numpy as np
import time
import cv2
import os
from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt 

# Define our imshow function 
def imshow(title = "Image", image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

# Download and unzip our images and YOLO files
!wget https://moderncomputervision.s3.eu-west-2.amazonaws.com/NeuralStyleTransfer.zip
!unzip -qq NeuralStyleTransfer.zip

!wget https://github.com/rajeevratan84/ModernComputerVision/raw/main/city.jpg

# Load our t7 neural transfer models
model_file_path = "NeuralStyleTransfer/models/"
model_file_paths = [f for f in listdir(model_file_path) if isfile(join(model_file_path, f))]

# Load our test image
img = cv2.imread("city.jpg")

# Loop through and applying each model style our input image
for (i,model) in enumerate(model_file_paths):
    # print the model being used
    print(str(i+1) + ". Using Model: " + str(model)[:-3])    
    style = cv2.imread("NeuralStyleTransfer/art/"+str(model)[:-3]+".jpg")
    # loading our neural style transfer model 
    neuralStyleModel = cv2.dnn.readNetFromTorch(model_file_path+ model)

    # Let's resize to a fixed height of 640 (feel free to change)
    height, width = int(img.shape[0]), int(img.shape[1])
    newWidth = int((640 / height) * width)
    resizedImg = cv2.resize(img, (newWidth, 640), interpolation = cv2.INTER_AREA)

    # Create our blob from the image and then perform a forward pass run of the network
    inpBlob = cv2.dnn.blobFromImage(resizedImg, 1.0, (newWidth, 640), (103.939, 116.779, 123.68), swapRB=False, crop=False)

    neuralStyleModel.setInput(inpBlob)
    output = neuralStyleModel.forward()

    # Reshaping the output tensor, adding back  the mean subtraction and re-ordering the channels 
    output = output.reshape(3, output.shape[2], output.shape[3])
    output[0] += 103.939
    output[1] += 116.779
    output[2] += 123.68
    output /= 255
    output = output.transpose(1, 2, 0)
    
    #Display our original image, the style being applied and the final Neural Style Transfer
    imshow("Original", img)
    imshow("Style", style)
    imshow("Neural Style Transfers", output)

# Load our t7 neural transfer models
model_file_path = "NeuralStyleTransfer/models/ECCV16/"
model_file_paths = [f for f in listdir(model_file_path) if isfile(join(model_file_path, f))]

# Load our test image
img = cv2.imread("city.jpg")

# Loop through and applying each model style our input image
for (i,model) in enumerate(model_file_paths):
    # print the model being used
    print(str(i+1) + ". Using Model: " + str(model)[:-3])    
    style = cv2.imread("NeuralStyleTransfer/art/"+str(model)[:-3]+".jpg")
    # loading our neural style transfer model 
    neuralStyleModel = cv2.dnn.readNetFromTorch(model_file_path+ model)

    # Let's resize to a fixed height of 640 (feel free to change)
    height, width = int(img.shape[0]), int(img.shape[1])
    newWidth = int((640 / height) * width)
    resizedImg = cv2.resize(img, (newWidth, 640), interpolation = cv2.INTER_AREA)

    # Create our blob from the image and then perform a forward pass run of the network
    inpBlob = cv2.dnn.blobFromImage(resizedImg, 1.0, (newWidth, 640), (103.939, 116.779, 123.68), swapRB=False, crop=False)

    neuralStyleModel.setInput(inpBlob)
    output = neuralStyleModel.forward()

    # Reshaping the output tensor, adding back  the mean subtraction and re-ordering the channels 
    output = output.reshape(3, output.shape[2], output.shape[3])
    output[0] += 103.939
    output[1] += 116.779
    output[2] += 123.68
    output /= 255
    output = output.transpose(1, 2, 0)
    
    #Display our original image, the style being applied and the final Neural Style Transfer
    imshow("Original", img)
    imshow("Style", style)
    imshow("Neural Style Transfers", output)

# Load our t7 neural transfer models
model_file_path = "NeuralStyleTransfer/models/ECCV16/starry_night.t7"

# Load video stream, long clip
cap = cv2.VideoCapture('dj.mp4')

# Get the height and width of the frame (required to be an interger)
w = int(cap.get(3)) 
h = int(cap.get(4))

# Define the codec and create VideoWriter object. The output is stored in '*.avi' file.
out = cv2.VideoWriter('NST_Starry_Night.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (w, h))

# Loop through and applying each model style our input image
#for (i,model) in enumerate(model_file_paths):
style = cv2.imread("NeuralStyleTransfer/art/starry_night.jpg")
i = 0
while(1):

    ret, img = cap.read()

    if ret == True:  
      i += 1
      print("Completed {} Frame(s)".format(i))
      # loading our neural style transfer model 
      neuralStyleModel = cv2.dnn.readNetFromTorch(model_file_path)

      # Let's resize to a fixed height of 640 (feel free to change)
      height, width = int(img.shape[0]), int(img.shape[1])
      newWidth = int((640 / height) * width)
      resizedImg = cv2.resize(img, (newWidth, 640), interpolation = cv2.INTER_AREA)

      # Create our blob from the image and then perform a forward pass run of the network
      inpBlob = cv2.dnn.blobFromImage(resizedImg, 1.0, (newWidth, 640),
                                (103.939, 116.779, 123.68), swapRB=False, crop=False)

      neuralStyleModel.setInput(inpBlob)
      output = neuralStyleModel.forward()

      # Reshaping the output tensor, adding back  the mean subtraction 
      # and re-ordering the channels 
      output = output.reshape(3, output.shape[2], output.shape[3])
      output[0] += 103.939
      output[1] += 116.779
      output[2] += 123.68
      output /= 255
      output = output.transpose(1, 2, 0)
      
      #Display our original image, the style being applied and the final Neural Style Transfer
      #imshow("Original", img)
      #imshow("Style", style)
      #imshow("Neural Style Transfers", output)
      vid_output = (output * 255).astype(np.uint8)
      vid_output = cv2.resize(vid_output, (w, h), interpolation = cv2.INTER_AREA)
      out.write(vid_output)
    else:
      break

cap.release()
out.release()

!ffmpeg -i /content/NST_Starry_Night.avi NST_Starry_Night.avi -y

from IPython.display import HTML
from base64 import b64encode
 
video_path = '/content/NST_Starry_Night.avi'
 
mp4 = open(video_path, "rb").read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML(f"""
<video width=600 controls><source src="{data_url}" type="video/mp4">
</video>""")