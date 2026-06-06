# AirDraw: Real-Time Virtual Drawing Board Using OpenCV Color Tracking

## Overview

AirDraw is a real-time computer vision application developed using Python, OpenCV, and NumPy. The system uses a webcam to detect and track a green-colored object, allowing users to draw on a virtual canvas without using a mouse or touchscreen.

The project demonstrates how computer vision techniques such as color segmentation, contour detection, object tracking, and real-time image processing can be used to create an interactive drawing application.

---

## Features

- Real-time webcam video processing
- Green object detection and tracking
- Virtual drawing canvas
- Multiple drawing colors
- Eraser mode
- Pause and draw mode
- Canvas clearing function
- User-friendly keyboard controls
- No external datasets or image files required

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Main programming language |
| OpenCV | Video capture and image processing |
| NumPy | Array and image manipulation |

---

## System Workflow

1. Capture live video from the webcam using OpenCV.
2. Convert each frame from BGR color space to HSV color space.
3. Detect the green object using color thresholding.
4. Find the largest contour corresponding to the tracked object.
5. Calculate the center position of the object.
6. Use the center position as a virtual pen.
7. Draw lines on a digital canvas based on object movement.
8. Display the updated drawing in real time.

---

## Project Architecture

```text
Webcam
   ↓
OpenCV Video Capture
   ↓
HSV Color Conversion
   ↓
Green Object Detection
   ↓
Contour Detection
   ↓
Center Point Tracking
   ↓
Drawing Logic
   ↓
Virtual Canvas Output
```

---

## Color Tracking

The system tracks a green-colored object using the HSV color space.

The processing steps are:

- Convert the webcam frame to HSV format.
- Apply color thresholding to isolate green pixels.
- Remove noise using erosion and dilation.
- Detect contours in the thresholded image.
- Track the center of the largest detected contour.

The tracked center point is used as a virtual pen for drawing.

---

## Keyboard Controls

| Key | Function |
|------|----------|
| D | Enable Drawing |
| P | Pause Drawing |
| B | Blue Drawing Color |
| G | Green Drawing Color |
| R | Red Drawing Color |
| E | Eraser Mode |
| C | Clear Canvas |
| Q | Quit Application |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AirDraw.git
cd AirDraw
```

### Install Dependencies

```bash
pip install opencv-python numpy
```

---

## Run the Application

```bash
python3 airdraw.py
```

---

## Project Structure

```text
AirDraw/
│
├── airdraw.py
├── README.md
└── screenshots/
```

---

## Example Usage

1. Start the application.
2. Hold a green object in front of the webcam.
3. Move the object to draw on the canvas.
4. Change drawing colors using keyboard shortcuts.
5. Use pause mode when repositioning the object.
6. Use eraser mode when needed.
7. Clear the canvas or exit the application.

---

## Results


|                                   |                                    |
| --------------------------------- | ---------------------------------- |
| ![AirDraw Demo](airdraw_demo.gif) | ![AirDraw Demo](airdraw_demo2.gif) |


### Full Drawing Video

[▶ Download / Watch Full Video](demo/airdraw_demo.mp4)


---

## Computer Vision Concepts Used

This project applies several important computer vision techniques:

- Real-Time Video Processing
- HSV Color Space Conversion
- Color Segmentation
- Contour Detection
- Object Tracking
- Image Drawing and Overlay
- Human-Computer Interaction

---

## Challenges

During development, several challenges were encountered:

- Maintaining stable color detection under different lighting conditions
- Reducing drawing jitter caused by rapid object movement
- Improving object tracking accuracy
- Implementing pause and drawing modes for better usability

---

## Future 

Future versions of AirDraw can be updated:

- Multi-color object tracking
- Shape recognition
- Save drawing as image
- Gesture-based controls
- Virtual whiteboard collaboration
- AI-powered handwriting recognition

---

## Project Motivation

The goal of this project is to explore computer vision techniques and develop an interactive drawing application using object tracking technology. AirDraw demonstrates how webcam-based systems can be used to create intuitive and engaging human-computer interaction.

---


**Seng Cyn Mai**  
