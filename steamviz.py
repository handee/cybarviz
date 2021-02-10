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



blue=(170, 172, 128)
magenta=(59, 47, 110)
orange=(120, 217, 253)
green=(66, 85, 96)
h=1920
w=1080
c=3

def steampunk(img):
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(grey, thrs1, thrs2, apertureSize=5)
    vis = img.copy()

    vis[edge != 0] = magenta
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
        vis=steampunk(img)
        cv.imshow('edge', vis)
        ch = cv.waitKey(5)
        if ch == 27:
            break
    cv.destroyAllWindows()

