import cv2

# Image Load
img = cv2.imread("images/test.jpg")

# Resize
img = cv2.resize(img, (800, 600))

# Grayscale
gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

# Blur
blur = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)

# Threshold
thresh = cv2.adaptiveThreshold(
    blur,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# Invert
thresh = cv2.bitwise_not(thresh)

cv2.imshow("Original", img)
cv2.imshow("Sketch", thresh)

cv2.imwrite(
    "clean_sketch.png",
    thresh
)

cv2.waitKey(0)
cv2.destroyAllWindows()