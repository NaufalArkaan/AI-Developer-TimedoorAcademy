import cv2
import mediapipe as mp
import math
from math import hypot

cap = cv2.VideoCapture(0)
nose_img = cv2.imread('./Face_Filter/mouth.png')
cap.set(3, 950)  # width
cap.set(4, 900)  # height

mpDrawingStyles = mp.solutions.drawing_styles
mpFaceMesh = mp.solutions.face_mesh
mpDraw = mp.solutions.drawing_utils  # This line was missing
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=4)
print(math.hypot(3, 4))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(rgb)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            leftnosex = leftnosey = rightnosex = rightnosey = centernosex = centernosey = 0
            for lm_id, lm in enumerate(face_landmarks.landmark):
                h, w, c = frame.shape
                x, y = int(lm.x * w), int(lm.y * h)
                if lm_id == 409:  # landmark bagian kiri hidung
                    leftnosex, leftnosey = x, y
                if lm_id == 450:  # landmark bagian kanan hidung
                    rightnosex, rightnosey = x, y
                if lm_id == 4:  # landmark bagian Tengah hidung
                    centernosex, centernosey = x, y

            nose_width = int(hypot(rightnosex - leftnosex, rightnosey - leftnosey * 1.2))
            nose_height = int(nose_width * 0.8)

            if nose_width != 0 and nose_height != 0:
                pig_nose = cv2.resize(nose_img, (nose_width, nose_height))

                top_left = (int(centernosex - nose_width / 2), int(centernosey - nose_height / 5))
                bottom_right = (int(centernosex + nose_width / 2), int(centernosey + nose_height / 2))

                nose_area = frame[top_left[1]: top_left[1] + nose_height, top_left[0]: top_left[0] + nose_width]

                pig_nose_gray = cv2.cvtColor(pig_nose, cv2.COLOR_BGR2GRAY)
                _, nose_mask = cv2.threshold(pig_nose_gray, 25, 255, cv2.THRESH_BINARY_INV)

                no_nose = cv2.bitwise_and(nose_area, nose_area, mask=nose_mask)
                final_nose = cv2.add(no_nose, pig_nose)

                frame[top_left[1]: top_left[1] + nose_height, top_left[0]: top_left[0] + nose_width] = final_nose

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
