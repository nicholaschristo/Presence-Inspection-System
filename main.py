import cv2

# Open USB camera
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# ROI (Region of Interest)
roi_x = 200
roi_y = 150
roi_w = 250
roi_h = 150

while True:

    # Capture frame
    ret, frame = cap.read()

    # Check frame
    if not ret:
        print("Failed to grab frame")
        break

    # Draw ROI box (Blue)
    cv2.rectangle(
        frame,
        (roi_x, roi_y),
        (roi_x + roi_w, roi_y + roi_h),
        (255, 0, 0),
        2
    )

    # Crop ROI
    roi = frame[
        roi_y:roi_y + roi_h,
        roi_x:roi_x + roi_w
    ]

    # Step 1 - Convert to grayscale
    gray = cv2.cvtColor(
        roi,
        cv2.COLOR_BGR2GRAY
    )

    # Step 2 - Gaussian Blur
    blur = cv2.GaussianBlur(
        gray,
        (5,5),
        0
    )

    # Step 3 - Thresholding
    _, thresh = cv2.threshold(
        blur,
        100,
        255,
        cv2.THRESH_BINARY_INV
    )

    # Step 4 - Find contours
    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Default status every frame
    status = "NG"

    # Step 5 - Process contours
    for cnt in contours:

        # Contour area
        area = cv2.contourArea(cnt)

        # Filter tiny noise
        if 1000 < area < 5000:

            # Bounding rectangle
            x, y, w, h = cv2.boundingRect(cnt)

            # Additional filtering
            if w > 50 and h > 20:

                # Object detected
                status = "OK"

                # Draw bounding box
                cv2.rectangle(
                    frame,
                    (x + roi_x, y + roi_y),
                    (x + w + roi_x, y + h + roi_y),
                    (0,255,0),
                    2
                )

    # Display OK / NG status
    cv2.putText(
        frame,
        f"STATUS: {status}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0) if status == "OK" else (0,0,255),
        2
    )

    # Show threshold image
    cv2.imshow("Threshold", thresh)

    # Show inspection system
    cv2.imshow(
        "Inspection System",
        frame
    )

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release camera
cap.release()

# Close all windows
cv2.destroyAllWindows()