import cv2
import numpy as np
from collections import deque
import warnings
warnings.filterwarnings("ignore")

import config
from hand_tracker import HandTracker
from gesture_utils import is_draw, is_pause, is_erase
from grid_utils import draw_grid
from toolbar_utils import draw_toolbar, check_toolbar_click
from ocr_utils import recognize_text

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

tracker = HandTracker()
canvas = np.zeros((720, 1280, 3), dtype=np.uint8)

points = deque(maxlen=config.SMOOTHING)
current_color = config.COLORS[config.DEFAULT_COLOR]
eraser_mode = False

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.flip(img, 1)
    tracker.process(img)
    lm = tracker.get_landmarks(img)

    if lm:
        x, y = lm[8][1], lm[8][2]

        # Toolbar interaction
        tool = check_toolbar_click(x, y)
        if tool:
            if tool[0] == "color":
                current_color = config.COLORS[tool[1]]
                eraser_mode = False
            elif tool[0] == "eraser":
                eraser_mode = True
            elif tool[0] == "save":
                cv2.imwrite(config.SAVE_IMAGE_NAME, canvas)
                print("Saved:", config.SAVE_IMAGE_NAME)

        elif is_draw(lm):
            points.append((x, y))
            for i in range(1, len(points)):
                if eraser_mode:
                    cv2.circle(
                        canvas, points[i],
                        config.ERASER_SIZE, (0, 0, 0), -1
                    )
                else:
                    cv2.line(
                        canvas,
                        points[i - 1],
                        points[i],
                        current_color,
                        config.BRUSH_SIZE
                    )

        elif is_erase(lm):
            cv2.circle(
                canvas, (x, y),
                config.ERASER_SIZE, (0, 0, 0), -1
            )
            points.clear()

        elif is_pause(lm):
            points.clear()

    img = draw_grid(img)
    img = draw_toolbar(img, None)
    img = cv2.add(img, canvas)

    cv2.imshow("AI Air Writing System", img)

    # ⌨ KEY CONTROLS (MUST BE INSIDE LOOP)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('t'):   # OCR trigger
        print("\n--- OCR OUTPUT ---")
        print(recognize_text(canvas))
        print("------------------")

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()