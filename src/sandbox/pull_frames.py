import numpy as np
import cv2

cap = cv2.VideoCapture(0)

frames_skipped = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)

    key = cv2.waitKey(100)
    print(key)
    # 32 is spacebar, 2 is left arrow, 3 is right arrow
    # 27 is escape
    if key == 27: break

    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
