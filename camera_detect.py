import cv2

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    # SPACE = Capture + Detect
    if key == 32:

        cv2.imwrite("capture.jpg", frame)

        img = cv2.imread("capture.jpg")

        img = cv2.resize(img, (800, 600))

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        blur = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

        thresh = cv2.adaptiveThreshold(
            blur,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

        thresh = cv2.bitwise_not(thresh)

        cv2.imwrite(
            "clean_sketch.png",
            thresh
        )

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        output = cv2.cvtColor(
            thresh,
            cv2.COLOR_GRAY2BGR
        )

        objects = []

        for contour in contours:

            area = cv2.contourArea(contour)

            if area < 50:
                continue

            x, y, w, h = cv2.boundingRect(
                contour
            )

            label = "Unknown"

            if area > 30000:
                label = "House"

            elif h > w:
                label = "Tree"

            if label != "Unknown":
                objects.append(label)

            cv2.rectangle(
                output,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                output,
                label,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        # Remove duplicates
        objects = list(set(objects))

        print("\nDetected Objects:")
        print(objects)

        # Prompt Generator
        if "House" in objects and "Tree" in objects:

            prompt = """
A beautiful countryside house beside a large green tree,
photorealistic, ultra detailed, cinematic lighting,
high quality, realistic environment
"""

        elif "House" in objects:

            prompt = """
A beautiful realistic house,
photorealistic, ultra detailed
"""

        elif "Tree" in objects:

            prompt = """
A large green tree in nature,
photorealistic, ultra detailed
"""

        else:

            prompt = """
A realistic outdoor scene
"""

        print("\nGenerated Prompt:\n")
        print(prompt)

        # Save prompt
        with open(
            "prompt.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(prompt)

        print("\nPrompt saved to prompt.txt")

        cv2.imshow(
            "Detection Result",
            output
        )

    # ESC = Exit
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()