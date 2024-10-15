import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3)) 
    height = int(cap.get(4))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # HSV -> HUE , SATURATION , BRIGHTNESS OR LIGHTNESS (VISIBILITY)
    # HUE = COLOR , SATURATION = RED , LIGHTNESS = BLACK TO WHITE SCALE
    
    light_blue = np.array([90,50,50])
    thick_blue = np.array([130,255,255])
    #inRange returns binary values 1 - color found(white) , 0 - not founded(black)
    mask = cv2.inRange(hsv,light_blue,thick_blue)
    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',result)
    #cv2.imshow('frame',result)
    

    if cv2.waitKey(1) == ord('q'):
        
        break

cap.release()
cv2.destroyAllWindows()