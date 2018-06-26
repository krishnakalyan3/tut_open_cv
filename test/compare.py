#!/usr/bin/env python3

import cv2
import numpy as np

eye = cv2.imread('../data/image001.png')
mask1 = cv2.imread('../data/image001_hem.png')
mask2 = cv2.imread('../data/mask3.png')

weighted = cv2.addWeighted(eye, 0.6, mask2, 0.4, 0)


cv2.imshow('add', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
