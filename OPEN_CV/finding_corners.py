import numpy as np
import cv2
import random

img = cv2.imread(r"C:\Users\spdre\Documents\CODINGS\OPEN_CV\files\chess_board.jpg",1)  
img = cv2.resize(img,(0,0),fx=0.50,fy=0.50)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#source,number_of_corners_minimum_quality,Minumum distance
corners = cv2.goodFeaturesToTrack(gray,500,0.7,100)
#above functions returning float values

corners = np.int0(corners)

#for loop draw a circle at the corners
#ravel method is used to change a multi_dimensional array into flatted array
for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),4,(0,255,0),-1)

#Below function draw lines between points
#since corners array-> [[x,y]] -> [i][0] access = [x,y] 
for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1= tuple(corners[i][0])
        corner2= tuple(corners[j][0])
        #color = tuple(map(lambda x: int(x),np.random.randint(0,255,size=3)))
        #img = cv2.line(img,corner1,corner2,color,1)
        img = cv2.line(img,corner1,corner2,(0,255,255),1)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()