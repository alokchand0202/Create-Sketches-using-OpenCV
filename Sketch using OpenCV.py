# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 23:53:55 2019

@author: alokc
"""
%reset -f
import cv2
import numpy as np

# Our sketch generating function
def create_sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 20, 75)
    
    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


#Read data from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Sketch', create_sketch(frame))
    if cv2.waitKey(1) == 13: 
        break
        
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()  
