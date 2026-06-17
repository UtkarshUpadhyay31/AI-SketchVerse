import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector(
    detectionCon=0.8,
    maxHands=1
)

while True:

    success, img = cap.read()

    if not success:
        break

    hands, img = detector.findHands(img)

    if hands:

        hand = hands[0]

        lmList = hand["lmList"]

        for point in lmList:

            x, y, z = point

            cv2.circle(
                img,
                (x, y),
                5,
                (0, 255, 0),
                -1
            )

    cv2.imshow(
        "Hand Tracking",
        img
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()