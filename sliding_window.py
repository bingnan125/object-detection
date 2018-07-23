# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:00:08 2018

@author: Bona
"""

import imutils
def pyramid(image,scale=1.5,minSize=(30,30)):
    '''
    scale:how much the image is resized at each layer
    minSize:the minimum required width and height of the layer
    '''
    #yield the original image in the pyramid(the bottom layer)
    yield image
    
    #keep looping over the pyramid
    while True:
        #compute the size of the image in the next layer of the pyramid
        w = int(image.shape[1] / scale)
        image = imutils.resize(image,width=w)
        
        #if the resized image does not meet the supplied minimum size,
        #then stop constructing the pyramid
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break
        
        #yield the next image in the pyramid
        yield image
        
def sliding_window(image,stepSize,windowSize):
    '''
    stepSize:how many pixels we are going to skip in both the (x,y) direction
    windowSize:the width and height of the window we are going to extract from image
    '''
    #slide a window across the image
    for y in range(0,image.shape[0],stepSize):
        for x in range(0,image.shape[1],stepSize):
            #yield the current window
            yield (x,y,image[y:y+windowSize[1],x:x+windowSize[0]])
        
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Path to the image')
args = vars(ap.parse_args())

#load the image and define the window width and height
image = cv2.imread(args['image'])
(winW,winH)=(128,128)

#loop over the image pyramid
for resized in pyramid(image,scale=1.5):
    #loop over the sliding window for each layer of the paramid
    for (x,y,window) in sliding_window(resized,stepSize=32,windowSize=(winW,winH)):
        #if the window does not meet our desired window size,ignore it
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
        
        #since we do not have a classifier,we'll just draw the window
        clone = resized.copy()
        cv2.rectangle(clone,(x,y),(x+winW,y+winH),(0,255,0),2)
        cv2.imshow('window',clone)
        cv2.waitKey(1)
        time.sleep(0.2)
    
