# ocr_utils.py  (EASYOCR VERSION – NO TESSERACT)

import cv2
import easyocr
import numpy as np

# Load OCR reader once (English)
reader = easyocr.Reader(['en'], gpu=False)

def recognize_text(canvas):
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
    
    results = reader.readtext(th)
    
    text = ""
    for (_, txt, conf) in results:
        if conf > 0.3:
            text += txt + " "
    
    return text.strip()