import cv2
import numpy as np

print("Video")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2, cv2.COLOR_BGR2GRAY)
    cv2.imgshow('frame', 'gray')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
