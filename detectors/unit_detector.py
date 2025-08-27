import os
import numpy as np
from detectors.onnx_detector import OnnxDetector
from detectors.side_detector import SideDetector
from namespaces.units import Position
from namespaces.units import UnitDetection
import constants


class UnitDetector(OnnxDetector):
    MIN_CONF = 0.45
    UNIT_Y_START = 0.05
    UNIT_Y_END = 0.80

    def __init__(self, model_path, cards):
        super().__init__(model_path)
        self.cards = cards

        self.side_detector = SideDetector(
            os.path.join(constants.MODELS_DIR, "side.onnx")
        )
        self.possible_ally_names = self._get_possible_ally_names()

    @staticmethod
    def _get_tile_xy(bbox):
        # x = (bbox[0] + bbox[2]) * DISPLAY_WIDTH / (2 * SCREENSHOT_WIDTH)
        # y = bbox[3] * DISPLAY_HEIGHT / SCREENSHOT_HEIGHT
        # tile_x = round(((x - TILE_INIT_X) / TILE_WIDTH) - 0.5)
        # tile_y = round(
        #     ((DISPLAY_HEIGHT - TILE_INIT_Y - y) / TILE_HEIGHT) - 0.5
        # )
        return 1, 1

    def _get_possible_ally_names(self):
        possible_ally_names = set()
        for card in self.cards:
            for unit in card.units:
                possible_ally_names.add(unit.name)
        return possible_ally_names

    def _calculate_side(self, image, bbox, name):
        if name not in self.possible_ally_names:
            side = "enemy"
        else:
            crop = image.crop(bbox)
            side = self.side_detector.run(crop)
        return side

    def _preprocess(self, image):
        image = image.crop(
            (
                0,
                self.UNIT_Y_START * image.height,
                image.width,
                self.UNIT_Y_END * image.height,
            )
        )
        image, padding = self.resize_pad_transpose_and_scale(image)
        image = np.expand_dims(image, axis=0)
        return image, padding

    def _post_process(self, pred, height, image):
        pred[:, [1, 3]] *= self.UNIT_Y_END - self.UNIT_Y_START
        pred[:, [1, 3]] += self.UNIT_Y_START * height

        allies = []
        enemies = []
        for p in pred:
            l, t, r, b, conf, cls = p
            bbox = (round(l), round(t), round(r), round(b))
            tile_x, tile_y = self._get_tile_xy(bbox)
            position = Position(bbox, conf, tile_x, tile_y)
            unit = constants.DETECTOR_UNITS[int(cls)]
            unit_detection = UnitDetection(unit, position)

            side = self._calculate_side(image, bbox, unit.name)
            if side == "ally":
                allies.append(unit_detection)
            else:
                enemies.append(unit_detection)

        return allies, enemies

    def run(self, image):
        height, width = image.height, image.width
        np_image, padding = self._preprocess(image)
        pred = self._infer(np_image)[0]
        pred = pred[pred[:, 4] > self.MIN_CONF]
        pred = self.fix_bboxes(pred, width, height, padding)
        allies, enemies = self._post_process(pred, height, image)
        return allies, enemies