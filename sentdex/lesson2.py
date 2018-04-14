#!/usr/bin/env python3

import cv2, numpy

# Webcam 0
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../data/output1.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
