#!/usr/bin/env python3


import cv2

IMG_LOC = '../data/image1.jpg'

img = cv2.imread(IMG_LOC, cv2.IMREAD_COLOR)
px = img[55,55]
img[55,55] = [255,255, 255]

# ROI region of image
#img[1000:150, 100:1500] = [255, 255, 255]

some_region = img[0:500, 0:500]
img[200:700, 200:700] = some_region

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
