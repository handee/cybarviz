#!/usr/bin/env python

'''
cybar smoke and mirrors
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2 as cv
import numpy as np

# relative module
import video

# built-in module
import sys
import random



blue=(255, 175, 0)
magenta=(255, 0, 255)
orange=(69, 117, 255)
green=(132, 246, 78)
h=1920
w=1080
c=3

def edge(img):
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(grey, thrs1, thrs2, apertureSize=5)
    vis = img.copy()
    vis = np.uint8(vis/8.)
    vis[edge != 0] = blue 
    return vis

def process(img,which):
    vis=np.zeros((h,w,3),np.uint8)
    if (which==0):
       vis=edge(img)
    elif (which==1):
       vis=cv.imread('polybius.png')
    elif (which==2):
       vis=cv.imread('polybius2.png')
    elif (which==3):
       vis[:,:]=orange
    elif (which==4):
       vis[:,:]=magenta
    elif (which==5):
       vis[:,:]=blue
    else:
       vis[:,:]=green
    return vis
 
if __name__ == '__main__':
    print(__doc__)

    try:
        fn = sys.argv[1]
    except:
        fn = 0

    def nothing(*arg):
        pass

    thrs1 = 800 
    thrs2 = 1000
    cv.namedWindow('edge')
    cap = video.create_capture(fn)
    while True:
        flag, img = cap.read()
	h,w,c=img.shape
        n=random.randint(0,7)
        vis=process(img,n)
        cv.imshow('edge', vis)
        ch = cv.waitKey(5)
        if ch == 27:
            break
    cv.destroyAllWindows()

