import cv2
import numpy as np

capture = cv2.VideoCapture(0)

red_lower = np.array([136, 87, 111])
red_upper = np.array([180, 255, 255])

while True:
    rate, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, red_lower, red_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Mask', mask)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(10) == ord('c'):
        break

capture.release()
cv2.destroyWindow()