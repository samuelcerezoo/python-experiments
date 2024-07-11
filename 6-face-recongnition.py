import numpy as np
import cv2

cap = cv2.VideoCapture(1) #access to the webcam

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# this two cascades return the location of the faces/eyes.


#loop until we press a key
while True:
    ret, frame = cap.read() #frame=image from the camera
    width = int(cap.get(3)) 
    height = int(cap.get(4))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255), 5)
        ROI_gray = gray[y:y+w, x:x+w] # because the eyes will be within the face area
        ROI_color = frame[y:y+w, x:x+w]
        eyes = eye_cascade.detectMultiScale(ROI_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(ROI_color, (ex, ey),(ex+ew, ey+eh),(255,0,0),5)




    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() #make the camera free to be used
cv2.destroyAllWindows()