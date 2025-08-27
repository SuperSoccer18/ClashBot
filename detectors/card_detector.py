import imagehash
import json
from utils import cv2_to_PIL
import numpy as np
from constants import cy1, cy2, cx1, cx2, cx3, cx4, cx5, cx6, cx7, cx8

# Handle card cycle detection + card selection for playing troops
class CardDetector:
    def __init__(self):
        self.known_hashes = self.get_known_hashes()
    
    # Get Hog 2.6 card hashes
    def get_known_hashes(self):
        with open("data/hog26_hashes.json", "r") as f:
            known_hashes_str = json.load(f)
        return {card_name: imagehash.hex_to_hash(phash_str) for card_name, phash_str in known_hashes_str.items()}

    # Grab cards from image
    def grab_cards(self, img):
        gamescreen = np.array(img)
        card1 = gamescreen[cy1:cy2, cx1:cx2]
        card2 = gamescreen[cy1:cy2, cx3:cx4]
        card3 = gamescreen[cy1:cy2, cx5:cx6]
        card4 = gamescreen[cy1:cy2, cx7:cx8]

        return [card1, card2, card3, card4]

    # Detect cards from image
    def detect_card(self, card_image):
        pil_img = cv2_to_PIL(card_image)
        card_phash = imagehash.phash(pil_img)

        best_match = None
        smallest_distance = float('inf')

        known_hashes = self.get_known_hashes()
        for card_name, phash in known_hashes.items():
            distance = card_phash - phash  # Hamming distance between hashes
            if distance < smallest_distance:
                smallest_distance = distance
                best_match = card_name

        # print(f"\nBest match: {best_match} (distance {smallest_distance})")
        return best_match
    
    # Return card dict
    def run(self, img):
        card_imgs = self.grab_cards(img)

        cards = {}
        for i in range(4):
            cards[f'Slot {i+1}'] = self.detect_card(card_imgs[i])
        return cards