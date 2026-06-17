import cv2

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key == 32:  # Space

        cv2.imwrite(
            "capture.jpg",
            frame
        )

        print("Image Captured!")

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()