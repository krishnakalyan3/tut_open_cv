#!/usr/bin/env python3

import cv2
import numpy as np

img1 = cv2.imread('../data/3D-Matplotlib.png')
img2 = cv2.imread('../data/mainsvmimage.png')


#add = img1+img2

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)


cv2.imshow('add', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
