import cv2
import numpy as np

def draw(canvas, x1, y1, x2, y2, color, size):
    cv2.line(canvas, (x1, y1), (x2, y2), color, size)

def erase(canvas, x, y, size):
    cv2.circle(canvas, (x, y), size, (0, 0, 0), -1)

def save(canvas):
    cv2.imwrite("air_writing_output.png", canvas)