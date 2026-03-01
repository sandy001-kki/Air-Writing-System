def finger_up(lm, tip, pip):
    return lm[tip][2] < lm[pip][2]

def is_draw(lm):
    return finger_up(lm, 8, 6) and not finger_up(lm, 12, 10)

def is_pause(lm):
    return finger_up(lm, 8, 6) and finger_up(lm, 12, 10)

def is_erase(lm):
    return (
        not finger_up(lm, 8, 6) and
        not finger_up(lm, 12, 10) and
        not finger_up(lm, 16, 14)
    )