import numpy as np
import cv2

'''classifier - already modeled , each classifier trained for different 
purposes
Hear Cascade: classifier (pre-rained) for eyes '''

cap = cv2.VideoCapture(0)
#path where it is stored on the system , spectific classifier
face_casecader = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_casecader = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret,frame = cap.read()
    #cv2.imshow('frame',frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #source,accuracy[lower the value , higher accuracy , slow speed],
    faces = face_casecader.detectMultiScale(gray,1.5,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w , y+h),(255,0,0),5)
        cv2.imshow('frame',frame)
        #for eyes
        ''' roi_gray = gray[y:y+w,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_casecader.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)
            cv2.imshow('frame',roi_color)'''

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows