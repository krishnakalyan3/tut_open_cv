#!/usr/bin/env python3.6



#from imutils import paths
#from imutils import paths
import argparse
import cv2


def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()


if __name__ == '__main__':
    IMG_LOC = '../data/2.jpg'
    image = cv2.imread(IMG_LOC)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    print(fm)

    cv2.putText(image, "Blur: {:.2f}".format( fm), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
