# Presence and Orientation Inspection System

## Overview

This project implements a real-time machine vision inspection system using OpenCV for industrial-style presence verification and orientation analysis.

The system captures live video from a USB camera, monitors a predefined inspection zone (ROI), detects objects placed inside the inspection area, calculates their orientation, and classifies them as Horizontal, Vertical, or Tilted.

The project simulates a basic machine vision inspection application commonly used in manufacturing, assembly verification, and quality control systems.

---

## Features

✅ Real-time USB camera acquisition

✅ ROI (Region of Interest) based inspection

✅ Grayscale image preprocessing

✅ Gaussian noise reduction

✅ Binary threshold segmentation

✅ Contour extraction and filtering

✅ Presence / Absence detection

✅ Angle measurement using OpenCV minAreaRect()

✅ Orientation classification

✅ Horizontal detection

✅ Vertical detection

✅ Tilted detection

✅ Industrial OK / NG decision logic

✅ Real-time visual feedback

---

## Technologies Used

- Python
- OpenCV
- NumPy
- USB Camera
- VS Code

---

## System Workflow

```text
Camera Feed
      ↓
ROI Selection
      ↓
Grayscale Conversion
      ↓
Gaussian Blur
      ↓
Thresholding
      ↓
Contour Detection
      ↓
Angle Measurement
      ↓
Orientation Classification
      ↓
OK / NG Decision
```

---

## Orientation Classification Logic

The detected object's orientation is classified based on the angle obtained from OpenCV's `minAreaRect()` function.

| Angle Range | Classification |
|------------|---------------|
| -20° to 20° | Horizontal |
| 70° to 110° | Vertical |
| Others | Tilted |

---

## Project Structure

```text
Presence-And-Orientation-Inspection-System
│
├── src
│   └── main.py
│
├── results
│   ├── horizontal_detection.png
│   ├── vertical_detection.png
│   ├── tilted_detection.png
│   └── no_object.png
│
├── demo
│   └── demo_video.mp4
│
└── README.md
```

---

## Test Objects

The system was tested using:

- Wall Plug
- Fasteners
- Small Industrial Components

These objects were chosen to simulate components commonly inspected in manufacturing and assembly environments.

---

## Sample Results

### Horizontal Detection

- Status: OK
- Orientation: HORIZONTAL

### Vertical Detection

- Status: OK
- Orientation: VERTICAL

### Tilted Detection

- Status: OK
- Orientation: TILTED

### No Object Present

- Status: NG
- Orientation: NONE

---

## Industrial Applications

This project demonstrates concepts used in:

- Assembly Verification
- Component Presence Detection
- Orientation Inspection
- Quality Control
- Machine Vision Systems
- Automated Inspection Stations
- Smart Manufacturing

---

## Skills Demonstrated

- Machine Vision Fundamentals
- Image Processing
- Industrial Inspection Logic
- Contour Analysis
- Angle Measurement
- ROI-Based Processing
- Real-Time Camera Applications
- OpenCV Development

---

## Future Improvements

- PLC Communication (Modbus TCP / Ethernet/IP)
- Reject Mechanism Simulation
- Defect Detection
- OCR / OCV Inspection
- AI-Based Object Detection
- Vision-Guided Robotics Integration
- OMRON Vision System Implementation
- Conveyor-Based Inspection

---

## Author

Nicholas Christo

B.Tech Computer Science Engineering (AI & ML)

Interested in:
- Machine Vision
- Industrial Automation
- Robotics
- Artificial Intelligence
- Vision-Guided Systems
