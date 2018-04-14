#!/usr/bin/env python3

import numpy as np
import cv2


img = cv2.imread('../data/image1.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (150, 150), (0, 0, 0), 15)
cv2.rectangle(img, (15, 25), (200, 150), (255, 255, 255), 5)
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)

pts = np.array([[10,4], [11, 54], [20, 30], [7, 11], [22, 14]], np.int32)
cv2.polylines(img, [pts], True, (0,255,0), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Open CV Tuts', (0, 130), font, 1, (0,0,0), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
