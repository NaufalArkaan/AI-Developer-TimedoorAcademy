import cv2
from tracker import EuclideanDistTracker
tracker = EuclideanDistTracker()

# Open the video file
cap = cv2.VideoCapture("./highway_tracker/highway.mp4")

# Create background subtractor
object_detector = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=200)

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Apply the background subtractor
    mask = object_detector.apply(frame)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:  # Filter out small contours
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the frame with contours
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask) #2 TAMBAHKAN CODE BARIS INI
    # Exit on pressing 'q'
    key = cv2.waitKey(30)
    if key == ord("q"):
        break

ret, frame = cap.read()
roi = frame[340:720, 500:800] #Dimensi lebar dari 500 - 800 & Dimensi tinggi dari 340 - 720
mask = object_detector.apply(roi)
_, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
# Release video capture object and close windows

detections = [[64, 311, 25, 69], [0, 266, 81, 114], [9, 326, 15, 26]] # add this line
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 100:
        x, y, w,h = cv2.boundingRect(cnt)
        detections.append([[0, 278, 89, 102], [2, 339, 17, 28]]) # add this line
        cv2.rectangle(detections)
print(detections)  # add this line

cap.release()
cv2.destroyAllWindows()
