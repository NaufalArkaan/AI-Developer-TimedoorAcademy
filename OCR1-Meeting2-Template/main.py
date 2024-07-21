from tensorflow.keras.models import load_model
from imutils.contours import sort_contours
import numpy as np
import imutils
import cv2

print("Load the model ....")
model = load_model("handwriting.model")
#Method load_model() bawaan library Tensorflow Keras digunakan untuk load Pre Trained Model OCR yang nanti akan disimpan kedalam variabel model

image = cv2.imread("images/2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow("Image", image)
cv2.waitKey(0)