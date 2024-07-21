import cv2  # explained in section a
import numpy as np

img = cv2.imread("meeting_7/exercise.jpg") # explained in section b
print(img.shape)

# Menggambar persegi
height, width, channel = img.shape
cv2.rectangle(img, (290, 40), (440,150),(0,255,0))
# cv2.line(img, (width,0), (0, height), (55,200,255), 3)
#memberikan inisial
img = cv2.putText(img, "Face", (290, 30), 
cv2.FONT_HERSHEY_COMPLEX, 1 , (86,255,86), 1)

# Menggambar persegi panjang
cv2.rectangle(img,(420, 260), (580, 380), (255,0,0), 1)
#memberikan inisial
img = cv2.putText(img, "Computer", (420, 250), 
cv2.FONT_HERSHEY_COMPLEX, 1 , (255,0,0), 1)

# Menggambar lingkaran
cv2.circle(img, (385, 380), 40, (0,0,255), 1)
#memberikan inisial
img = cv2.putText(img, "Coffe", (344, 338), 
cv2.FONT_HERSHEY_COMPLEX, 1 , (0,0,255), 1)

cv2.imshow("Image", img)  # explained in section c

cv2.waitKey(0)
cv2.destroyAllWindows() # explained in section d