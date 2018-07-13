# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:29:04 2018

@author: asus
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
        
from skimage.transform import pyramid_gaussian
import argparse
import cv2

#construct the argument parser and parser the arguments
ap =argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Path to the image')
ap.add_argument('-s','--scale',type=float,default=1.5,help='scale factor size')
args = vars(ap.parse_args())

#load the image
image = cv2.imread(args['image'])

#methon 1 :No smooth,just scaling
#loop over the image pyramid
for (i,resized) in enumerate(pyramid(image,scale=args['scale'])):
    #show the resized image
    cv2.imshow('Layer {}'.format(i+1),resized)
    cv2.waitKey(0)
    
#close all windows
#cv2.destoryAllWindows()

"""
#method 2:Resizing +Gaussian smothing
for (i,resized) in enumrate(pyramid_gaussian(image,downscale=2)):
    #if the image is too small,break from the loop
    if resized.shape[0]<30 or resized.shape[1] < 30:
        break
    
    #show the resized image
    cv2.inshow("Layer {}".format(i+1),resized)
    cv2.waitKey(0)
"""




















