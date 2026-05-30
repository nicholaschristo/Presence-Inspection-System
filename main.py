import cv2
import numpy as np

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

    if not ret:
        print("Failed to grab frame")
        break

    # Draw ROI
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

    # Convert to grayscale
    gray = cv2.cvtColor(
        roi,
        cv2.COLOR_BGR2GRAY
    )

    # Gaussian Blur
    blur = cv2.GaussianBlur(
        gray,
        (5,5),
        0
    )

    # Threshold
    _, thresh = cv2.threshold(
        blur,
        100,
        255,
        cv2.THRESH_BINARY_INV
    )

    # Find contours
    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Default values
    status = "NG"
    orientation = "NONE"
    detected_area = 0

    # Process contours
    for cnt in contours:

        area = cv2.contourArea(cnt)

        # Ignore tiny noise only
        if area > 1000:

            detected_area = area

            rect = cv2.minAreaRect(cnt)

            (center_x, center_y), (w, h), angle = rect

            if w > 50 and h > 20:

                status = "OK"

                # Rotated rectangle
                box = cv2.boxPoints(rect)
                box = np.int32(box)

                box[:,0] += roi_x
                box[:,1] += roi_y

                cv2.drawContours(
                    frame,
                    [box],
                    0,
                    (0,255,0),
                    2
                )

                # Normalize angle
                if w < h:
                    angle += 90

                # Orientation logic
                if -20 < angle < 20:
                    orientation = "HORIZONTAL"

                elif 70 < angle < 110:
                    orientation = "VERTICAL"

                else:
                    orientation = "TILTED"

                # Angle display
                cv2.putText(
                    frame,
                    f"Angle: {int(angle)}",
                    (20,80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255,255,0),
                    2
                )

                break

    # Status
    cv2.putText(
        frame,
        f"STATUS: {status}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0) if status == "OK" else (0,0,255),
        2
    )

    # Orientation
    cv2.putText(
        frame,
        f"Orientation: {orientation}",
        (20,120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    # Area display
    cv2.putText(
        frame,
        f"Area: {int(detected_area)}",
        (20,160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    # Show threshold image
    cv2.imshow("Threshold", thresh)

    # Show inspection system
    cv2.imshow(
        "Presence + Orientation Inspection",
        frame
    )

    # ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
