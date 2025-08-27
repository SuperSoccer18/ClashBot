from detectors.card_detector import CardDetector
from detectors.number_detector import NumberDetector
from detectors.unit_detector import UnitDetector
import constants
import os

class MainDetector:
    def __init__(self):
        self.card_detector = CardDetector()
        self.number_detector = NumberDetector()
        self.unit_detector = UnitDetector(os.path.join(constants.MODELS_DIR, 'units_M_480x352.onnx'), constants.hog_2_6_cards)

    def run(self, image):
        """
        Detect cards, numbers, and units in the given image.
        Returns a dictionary with detected items.
        """
        results = {
            'cards': self.card_detector.run(image),
            'numbers': self.number_detector.run(image),
            'units': self.unit_detector.run(image)
        }
        return results