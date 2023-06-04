import cv2
import numpy as np

camera = cv2.VideoCapture("How To Flirt Using Your Eyes.mp4")
while True:
    _, frame = camera.read()
    cv2.imshow('Camera', frame)
    edges = cv2.Canny(frame, 50, 50)
    cv2.imshow('Canny', edges)
    if cv2.waitKey(5) == ord('x'):
        break
camera.release()
cv2.destroyAllWindows()
