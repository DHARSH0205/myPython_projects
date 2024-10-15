import numpy as np
import cv2
import random

img = cv2.imread(r"C:\Users\spdre\Documents\CODINGS\OPEN_CV\files\chess_board.jpg",1)  
img = cv2.resize(img,(0,0),fx=0.50,fy=0.50)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray,100,0.7,50)

corners = np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),4,(0,255,0),-1)


for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1= tuple(corners[i][0])
        corner2= tuple(corners[j][0])

        img = cv2.line(img,corner1,corner2,(0,255,255),1)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()