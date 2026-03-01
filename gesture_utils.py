# gesture_utils.py

def finger_up(lm, tip, pip):
    return lm[tip][2] < lm[pip][2]

def is_draw(lm):
    # Index finger up, middle down
    return finger_up(lm, 8, 6) and not finger_up(lm, 12, 10)

def is_pause(lm):
    # Index + middle fingers up
    return finger_up(lm, 8, 6) and finger_up(lm, 12, 10)

def is_erase(lm):
    # Fist (all down)
    return (
        not finger_up(lm, 8, 6) and
        not finger_up(lm, 12, 10) and
        not finger_up(lm, 16, 14)
    )