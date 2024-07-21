import cv2
import numpy as np
img = cv2.imread('./ANPR_Python/images/shape.jpg')
imgGrayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                            |          |
#                            a          b
imgBlur = cv2.GaussianBlur(imgGrayScale, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50,50)
imgContours = img.copy()#a
def getContours(img):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)                                 
    for cnt in contours:   
        area = cv2.contourArea(cnt)
        print(area)                
    cv2.drawContours(imgContours, cnt, -1, (255,0,0), 3) 

getContours(imgCanny)

cv2.imshow("Contour Image", imgContours)
cv2.imshow("Original Picture", img)
cv2.imshow("Original Picture", img)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Gray Scale", imgGrayScale)
cv2.imshow("Canny Edge Detector", imgCanny)
cv2.waitKey(0)
