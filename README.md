# AirDraw: Real-Time Virtual Drawing Board Using Hand Tracking

## Overview

AirDraw is a real-time computer vision application developed using Python, OpenCV, and MediaPipe. The system uses a webcam to detect and track the user's hand movements, allowing the user to draw on a virtual canvas without touching any physical device.

The project demonstrates how computer vision techniques can be used to create natural human-computer interaction through hand tracking and gesture recognition.

---

## Features

- Real-time webcam video processing
- Hand detection and tracking
- Index finger tracking for drawing
- Multiple drawing colors
- Eraser mode
- Canvas clearing function
- User-friendly keyboard controls
- No external datasets or image files required

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Main programming language |
| OpenCV | Video capture and image processing |
| MediaPipe | Hand landmark detection and tracking |
| NumPy | Array and image manipulation |

---

## System Workflow

1. Capture live video from the webcam using OpenCV.
2. Detect the user's hand using MediaPipe Hands.
3. Identify hand landmarks and track the index finger tip.
4. Use fingertip coordinates as a virtual pen.
5. Draw lines on a digital canvas based on finger movement.
6. Display the updated drawing in real time.

---

## Project Architecture

```text
Webcam
   ↓
OpenCV Video Capture
   ↓
MediaPipe Hand Detection
   ↓
Hand Landmark Extraction
   ↓
Index Finger Tracking
   ↓
Drawing Logic
   ↓
Virtual Canvas Output
```

---

## Hand Landmark Detection

MediaPipe Hands detects 21 hand landmarks.

For this project:

- Landmark 8 → Index Finger Tip
- Landmark 12 → Middle Finger Tip

The system uses these landmarks to determine drawing actions and track finger movement accurately.

---

## Keyboard Controls

| Key | Function |
|------|----------|
| B | Blue Color |
| G | Green Color |
| R | Red Color |
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
pip install -r requirements.txt
```

Or install manually:

```bash
pip install opencv-python mediapipe numpy
```

---

## Run the Application

```bash
python main.py
```

---

## Project Structure

```text
AirDraw/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Example Usage

1. Start the application.
2. Position your hand in front of the webcam.
3. Move your index finger to draw.
4. Change colors using keyboard shortcuts.
5. Use eraser mode when needed.
6. Clear the canvas or exit the application.

---

## Results

### Drawing Example

![Drawing Example](screenshots/drawing1.png)

### Eraser Mode

![Eraser Mode](screenshots/drawing2.png)

---

## Computer Vision Concepts Used

This project applies several important computer vision techniques:

- Real-Time Video Processing
- Hand Detection
- Hand Landmark Tracking
- Gesture-Based Interaction
- Image Drawing and Overlay
- Human-Computer Interaction

---

## Challenges

During development, several challenges were encountered:

- Maintaining stable hand detection under different lighting conditions
- Reducing drawing delays during rapid hand movements
- Improving fingertip tracking accuracy
- Handling temporary hand occlusions

---

## Future Improvements

Future versions of AirDraw may include:

- Multiple hand support
- Shape recognition
- Save drawing as image
- Gesture-based color selection
- Virtual whiteboard collaboration
- AI-powered handwriting recognition

---

## Project Motivation

The goal of this project is to explore computer vision techniques and develop an interactive application using hand tracking technology. AirDraw demonstrates how webcam-based systems can replace traditional input devices and create a more natural user experience.

---

## Author

**Seng Cyn Mai**  
Computer Science Department  
Computer Vision Final Project
