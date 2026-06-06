import cv2
import numpy as np

cap = cv2.VideoCapture(1)

canvas = None
prev_x, prev_y = 0, 0

draw_color = (0, 255, 0)
brush_thickness = 8
eraser_thickness = 40

mode = "draw"
drawing_enabled = True

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot access webcam")
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest_contour) > 1000:
            x, y, width, height = cv2.boundingRect(largest_contour)
            center_x = x + width // 2
            center_y = y + height // 2

            cv2.circle(frame, (center_x, center_y), 10, draw_color, cv2.FILLED)

            if drawing_enabled:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = center_x, center_y

                if mode == "draw":
                    cv2.line(
                        canvas,
                        (prev_x, prev_y),
                        (center_x, center_y),
                        draw_color,
                        brush_thickness,
                    )

                elif mode == "erase":
                    cv2.line(
                        canvas,
                        (prev_x, prev_y),
                        (center_x, center_y),
                        (0, 0, 0),
                        eraser_thickness,
                    )

                prev_x, prev_y = center_x, center_y
            else:
                prev_x, prev_y = 0, 0
        else:
            prev_x, prev_y = 0, 0
    else:
        prev_x, prev_y = 0, 0

    gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, canvas_mask = cv2.threshold(gray_canvas, 20, 255, cv2.THRESH_BINARY)
    canvas_mask_inv = cv2.bitwise_not(canvas_mask)

    frame_bg = cv2.bitwise_and(frame, frame, mask=canvas_mask_inv)
    canvas_fg = cv2.bitwise_and(canvas, canvas, mask=canvas_mask)

    output = cv2.add(frame_bg, canvas_fg)

    status = "Drawing" if drawing_enabled else "Paused"

    cv2.putText(
        output,
        "AirDraw: OpenCV Virtual Drawing Board",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2,
    )

    cv2.putText(
        output,
        "Use a GREEN object to draw",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2,
    )

    cv2.putText(
        output,
        "D: Draw | P: Pause | B: Blue | G: Green | R: Red | E: Eraser | C: Clear | Q: Quit",
        (20, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2,
    )

    cv2.putText(
        output,
        f"Mode: {mode} | Status: {status}",
        (20, 145),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        draw_color,
        2,
    )

    cv2.imshow("AirDraw", output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("d"):
        drawing_enabled = True

    elif key == ord("p"):
        drawing_enabled = False
        prev_x, prev_y = 0, 0

    elif key == ord("b"):
        draw_color = (255, 0, 0)
        mode = "draw"
        drawing_enabled = True

    elif key == ord("g"):
        draw_color = (0, 255, 0)
        mode = "draw"
        drawing_enabled = True

    elif key == ord("r"):
        draw_color = (0, 0, 255)
        mode = "draw"
        drawing_enabled = True

    elif key == ord("e"):
        mode = "erase"
        drawing_enabled = True

    elif key == ord("c"):
        canvas = np.zeros_like(frame)
        prev_x, prev_y = 0, 0

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()