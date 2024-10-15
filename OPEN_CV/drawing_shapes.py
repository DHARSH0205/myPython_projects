import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #source,starting,ending,color,thickness(pixels) -> [drawing lines]
   
    img = cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    img = cv2.line(img,(0,height),(width,0),(255,0,0),10)

    #source,topleft,bottomRight,color,thickness
    # -1 means fill the shape with color
    img = cv2.rectangle(img,(50,50),(100,100),(0,255,0),3)

    #source,center_position,radius,color,thickness
    img = cv2.circle(img,(width//2,height//2),30,(0,0,255),10)

    '''(img,text,(starting_from[bottom,left],
     font,fontscale(thickness_of_font),color,thickness_of_border_text,linetype))'''
    
    font = cv2.FONT_ITALIC
    img = cv2.putText(img,'ITS DHARSH',(10,height),font,5,(0,255,100),10,cv2.LINE_AA)

    cv2.imshow('frame',img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows