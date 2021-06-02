import numpy as np
import cv2
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time

consecutive_none = 0
alarm = False
#eyes = 0
face = cv2.CascadeClassifier('HAAR_Files/haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('HAAR_Files/haarcascade_eye.xml')
img = cv2.imread('tejas.jpg')

vs = VideoStream(src=0).start()
time.sleep(1.0)

while True:
    num_eyes = 0
    frame = vs.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            num_eyes = num_eyes + 1
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    if num_eyes < 2:
        consecutive_none = consecutive_none + 1
        if not alarm:
            alarm = True
        if consecutive_none > 15:
            cv2.putText(frame, "ALERT! DROWSINESS DETECTED", (10, 30),
        				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        consecutive_none = 0
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
vs.stop()
