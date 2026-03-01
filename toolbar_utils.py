# toolbar_utils.py

import cv2
import config

TOOLBAR_HEIGHT = 80

def draw_toolbar(img, selected):
    x = 10
    for name, color in config.COLORS.items():
        cv2.rectangle(img, (x, 10), (x + 60, 60), color, -1)
        if name == selected:
            cv2.rectangle(img, (x, 10), (x + 60, 60), (255, 255, 255), 3)
        x += 70

    # Eraser
    cv2.rectangle(img, (x, 10), (x + 60, 60), (50, 50, 50), -1)
    cv2.putText(img, "E", (x + 18, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Save
    x += 70
    cv2.rectangle(img, (x, 10), (x + 60, 60), (0, 0, 0), -1)
    cv2.putText(img, "S", (x + 18, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return img


def check_toolbar_click(x, y):
    if y > 60:
        return None

    index = x // 70
    keys = list(config.COLORS.keys())

    if index < len(keys):
        return ("color", keys[index])

    if index == len(keys):
        return ("eraser", None)

    if index == len(keys) + 1:
        return ("save", None)

    return None