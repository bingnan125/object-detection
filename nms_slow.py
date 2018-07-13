# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:02:04 2018

@author: asus
"""
import numpy as np

#Felzenszwalb et al
def non_max_suppression_slow(boxes, overlapThresh):
    '''
    boxes:bounding boxes in the form of (startX,startY,endX,endY)
    overlapThresh:overlap threshold,normally between 0.3 and 0.5
    '''
    #if there are no boxes,return an empty list
    if len(boxes) == 0:
        return []
    
    #initialize the list of picked bounding boxes
    #the bounding boxes that we would like to keep,discard the rest
    pick =[]
    
    #grab the corrdinates of the bounding boxes
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    
    #compute the area of the bounding boxes and sort the bounding
    #boxes by the bottem-right y-coordinate of the bounding box
    area = (x2-x1+1)*(y2 - y1 +1)
    idxs = np.argsort(y2)    
    
    #keep looping while some indexes still remain in the indexes
    #list
    while len(idxs) > 0:
        #grab the last index in the indexes list,add the index
        #value to the list of picked indexes,then initialize
        #the suppression list(i.e. the list of boxes that will be deleted)
        #using the last index
        last = len(idxs)-1
        i = idxs[last]
        pick.append(i)
        suppress = [last]
        
        #loop over all indexes in the indexes list
        for pos in range(0,last):
            #grab the current index
            j = idxs[pos]
            
            #find the largest (x,y) coorfinates for the start of 
            #the bounding box and the smallest (x,y) coordinates
            #for the end of the bounding box
            xx1 = max(x1[i],x1[j])
            yy1 = max(y1[i],y1[j])
            xx2 = max(x2[i],x2[j])
            yy2 = max(y2[i],y2[j])
             
            #compute the width and height of the bounding box
            w = max(0,xx2 - xx1 + 1)
            h = max(0,yy2 - yy1 + 1)
            
            #compute the ratio of the overlap between the computed
            #bonding box and the bounding box in the area list
            overlap = float(w*h) / area[j]
            
            # if there is sufficient overlap,supress the current bounding box
            if overlap > overlapThresh:
                suppress.append(pos)
            
        #delete all indexes from index list that are in the suppression list
        idxs = np.delete(idxs,suppress)
            
    #return only the bounding boxes that were picked
    return boxes[pick]

import numpy as np
import cv2

#construct a list containing the images that will be examined
#along with their respective bounding boxes
images = []


#loop over the images
for (imagePath,boundingBoxes) in images:
    #load the image and clone it 
    print("[x] %d initial bounding boxes" %(len(boundingBoxes)))
    image = cv2.imread(imagePath)
    orig = image.copy()
    
    #loop over the bounding boxes for each image and draw them
    for (startX,startY,endX,endY) in boundingBoxes:
        cv2.rectangle(orig,(startX,startY),(endX,endY),(0,0,255),2)
        
    #preform non-maximum suppression on the bounding boxes
    pick = non_max_suppression_slow(boundingBoxes,0.3)
    print("[x] after applying non-maximum,%d bounding boxes" %(len(pick)))
    
    #loop over the picked bounding boxes and draw them
    for (startX,startY,endX,endY) in pick:
        cv2.rectangle(image,(startX,startY),(endX,endY),(0,255,0),2)
        
    #display the image
    cv2.imshow()
    cv2.imshow()
    cv.waitKey(0)




























    