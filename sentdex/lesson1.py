#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/image1.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Using Matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()

# Drawing a line
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80,100], 'c', linewidth=5)
plt.show()

# Write
cv2.imwrite('../data/watchgray.jpg', img)
