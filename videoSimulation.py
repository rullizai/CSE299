import numpy as np
import cv2

cap = cv2.VideoCapture("http://192.168.0.100:8080/video")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    # Display the resulting frame
    cv2.imshow('Video', ret)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
