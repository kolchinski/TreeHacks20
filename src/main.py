import cv2
from api_calls import text_from_image, read_text

cap = cv2.VideoCapture(0)

for i in range(10):
    print(i)

    ret, frame = cap.read()
    if not ret:
        print("Frame not read")
        continue

    frame_text = text_from_image(frame)
    print(frame_text)


    read_text(frame_text)


    cv2.imshow('frame', frame)

    key=cv2.waitKey(100)
    if key == 27: break





