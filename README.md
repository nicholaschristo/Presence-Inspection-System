# ROI-Based Presence Inspection System

## Overview

This project is a real-time industrial-style machine vision inspection system developed using Python and OpenCV.

The system detects the presence of an object inside a predefined Region of Interest (ROI) and provides an industrial-style OK/NG status output.

The project simulates the basic workflow used in industrial automation and machine vision applications such as:

- Presence/Absence Inspection
- Conveyor Inspection Systems
- Vision-Based Triggering
- Automated Quality Inspection
- Industrial Automation Integration

---

# Features

✅ Real-time USB camera inspection  
✅ ROI (Region of Interest) based detection  
✅ Threshold-based object segmentation  
✅ Contour detection and filtering  
✅ Noise reduction using Gaussian Blur  
✅ Shape and area filtering  
✅ Industrial-style OK / NG logic  
✅ Real-time visualization with bounding boxes  

---

# Technologies Used

- Python
- OpenCV
- VS Code

---

# Project Workflow

## 1. Image Acquisition
The system captures live video frames from a USB webcam.

## 2. ROI Selection
A fixed inspection region is defined to simulate industrial inspection zones.

## 3. Preprocessing
The captured frame undergoes:
- Grayscale conversion
- Gaussian Blur filtering

to improve image stability and reduce noise.

## 4. Threshold Segmentation
Binary inverse thresholding is applied to separate the object from the background.

## 5. Contour Detection
Contours are extracted from the threshold image.

## 6. Contour Filtering
Contours are filtered based on:
- Area
- Width
- Height

to reduce false detections.

## 7. Inspection Logic
If a valid object is detected inside the ROI:
- STATUS = OK

Otherwise:
- STATUS = NG

---

# Folder Structure

```text
PresenceInspectionSystem/
│
├── src/
│   └── main.py
│
├── screenshots/
│
├── demo/
│
└── README.md