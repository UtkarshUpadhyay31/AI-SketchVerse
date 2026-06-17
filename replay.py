import cv2
import numpy as np
import time

canvas = np.zeros(
    (600, 800, 3),
    dtype=np.uint8
)

points = []

with open("points.txt", "r") as f:

    for line in f:

        x, y = line.strip().split(",")

        points.append(
            (int(x), int(y))
        )

for i in range(1, len(points)):

    cv2.line(
        canvas,
        points[i - 1],
        points[i],
        (255, 255, 255),
        5
    )

    cv2.imshow(
        "Replay",
        canvas
    )

    cv2.waitKey(1)

    time.sleep(0.005)

cv2.waitKey(0)

cv2.destroyAllWindows()