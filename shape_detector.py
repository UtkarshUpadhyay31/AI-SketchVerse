import cv2

img = cv2.imread("clean_sketch.png", cv2.IMREAD_GRAYSCALE)

# binary image
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

detected_objects = []

for contour in contours:

    area = cv2.contourArea(contour)

    if area < 50:
        continue

    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

    x, y, w, h = cv2.boundingRect(contour)

    shape = "unknown"

    # triangle
    if len(approx) == 3:
        shape = "triangle"

    # rectangle / square
    elif len(approx) == 4:
        ratio = w / float(h)

        if 0.9 <= ratio <= 1.1:
            shape = "square"
        else:
            shape = "rectangle"

    # circle
    elif len(approx) > 8:
        shape = "circle"

    detected_objects.append(shape)

    cv2.rectangle(
        output,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        output,
        shape,
        (x, y - 5),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

print("Detected:", detected_objects)

cv2.imshow("Objects", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
with open("objects.txt", "w") as f:
    for obj in detected_objects:
        f.write(obj + "\n")

print("Saved objects.txt")