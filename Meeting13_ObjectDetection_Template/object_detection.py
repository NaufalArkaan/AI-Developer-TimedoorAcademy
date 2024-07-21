import numpy as np
import cv2

min_confidence = 0.6
net = cv2.dnn.readNetFromCaffe('models/MobileNetSSD_deploy.prototxt.txt','models/MobileNetSSD_deploy.caffemodel')
image = cv2.imread('images/1.jpg') # dijelaskan dibagian a
image = cv2.resize(image, (800, 600)) # dijelaskan dibagian b

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()