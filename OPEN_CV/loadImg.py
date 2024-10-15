import cv2
import random

img = cv2.imread(r"C:\Users\spdre\Documents\CODINGS\OPEN_CV\files\test.jpg",0)  
img = cv2.resize(img,(0,0),fx=0.75,fy=0.75)
#img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

#print(type(img))
#print(img.shape)
#print(img)

'''for i in range(1000):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        
tag = img[500:700,600:900]
img[100:300,500:800] = tag'''


#cv2.imwrite("new_img2.jpg",img)

#-1 cv2.IMREAD_COLOR
# 0 cv2.IMREAD_GRAYSCALE
# 1 cv2.IMREAD_UNCHANGED

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()