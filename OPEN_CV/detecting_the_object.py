import cv2
import numpy as np

img = cv2.resize(cv2.imread(r"C:\Users\spdre\Documents\CODINGS\OPEN_CV\files\soccer_practice.jpg",0),(0,0),fx=0.8,fy=0.8)
template=cv2.resize(cv2.imread(r"C:\Users\spdre\Documents\CODINGS\OPEN_CV\files\ball.png",0),(0,0),fx=0.8,fy=0.8)

#number of rows,number of coloumns
height , width = template.shape

#methods to detect the template in the base image
methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCOEFF_NORMED,
           cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

#for trying every methods
for method in methods:
    
    colorImg = cv2.resize(cv2.imread(r"C:\Users\spdre\Documents\CODINGS\OPEN_CV\files\soccer_practice.jpg",1),(0,0),fx=0.8,fy=0.8)
    img2  = img.copy()
    result = cv2.matchTemplate(img2,template,method)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
        
    bottom_right = (location[0] + width , location[1] + height)
    cv2.rectangle(colorImg,location,bottom_right,(100,200,23),9)
    cv2.imshow('Match',colorImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


