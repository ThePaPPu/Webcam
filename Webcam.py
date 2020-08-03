from functools import cached_property

import cv2

capture = cv2.VideoCapture(0)

while True:
    rate, frame = capture.read()
    cv2.imshow("Frame", frame)

    if cv2.waitKey(10) == ord('c'):
        break

capture.release()
cv2.destroyWindow()