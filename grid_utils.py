import cv2
import config

def draw_grid(img):
    h, w, _ = img.shape
    for y in range(0, h, config.GRID_SPACING):
        cv2.line(img, (0, y), (w, y), (50, 50, 50), 1)
    return img