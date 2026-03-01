import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.75,
            min_tracking_confidence=0.75
        )
        self.drawer = mp.solutions.drawing_utils
        self.results = None

    def process(self, img):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)

    def get_landmarks(self, img):
        lm = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]
            h, w, _ = img.shape
            for i, p in enumerate(hand.landmark):
                lm.append((i, int(p.x * w), int(p.y * h)))
            self.drawer.draw_landmarks(
                img, hand, self.mp_hands.HAND_CONNECTIONS
            )
        return lm