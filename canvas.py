import cv2
import numpy as np

drawing = False

last_x = None
last_y = None

# Drawing points store karne ke liye
points = []

canvas = np.zeros(
    (600, 800, 3),
    dtype=np.uint8
)

def draw(event, x, y, flags, param):

    global drawing
    global last_x
    global last_y
    global points

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True

        last_x = x
        last_y = y

        points.append((x, y))

    elif event == cv2.EVENT_MOUSEMOVE:

        if drawing:

            cv2.line(
                canvas,
                (last_x, last_y),
                (x, y),
                (255, 255, 255),
                5
            )

            # Point save karo
            points.append((x, y))

            last_x = x
            last_y = y

    elif event == cv2.EVENT_LBUTTONUP:

        drawing = False


cv2.namedWindow("Canvas")

cv2.setMouseCallback(
    "Canvas",
    draw
)

while True:

    cv2.imshow(
        "Canvas",
        canvas
    )

    key = cv2.waitKey(1)

    # Clear canvas
    if key == ord('c'):
        canvas[:] = 0
        points.clear()
        print("Canvas Cleared!")

    # Save image + points
    if key == ord('s'):

        cv2.imwrite(
            "drawing.png",
            canvas
        )

        with open("points.txt", "w") as f:

            for point in points:

                f.write(
                    f"{point[0]},{point[1]}\n"
                )

        print("Drawing and Points Saved!")

    # Exit
    if key == 27:
        break

cv2.destroyAllWindows()