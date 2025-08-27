import utils
import numpy as np
from PIL import ImageFilter
from constants import elixir_pixels, br, bl

# Handle all numerical data: elixir count, tower health, time?
class NumberDetector:
    def __init__(self):
        self.timer = 'Timer'    # initialize timer object; time.perf_counter()?

    # Calculate elixir bar pixels
    def calculate_elixir(self, img):
        gamescreen = utils.pil_to_cv2(img)
        elixir = 10
        while elixir > 0:
            # check corresponding elixir pixel for color
            b, g, r = gamescreen[1245, 550 - 40*(10-elixir)]
            if r > 100:
                break
            else:
                elixir -= 1
        return elixir
    
    # Calculate proportion of HP left from HP bar
    def calculate_hp(self, image, bbox, lhs_colour, rhs_colour, threshold=40):
        # image.crop(bbox).filter(ImageFilter.SMOOTH_MORE).show()
        crop = np.array(
            image.crop(bbox).filter(ImageFilter.SMOOTH_MORE), dtype=np.float32
        )

        means = np.array(
            [
                np.mean(np.abs(crop - colour), axis=2)
                for colour in [lhs_colour, rhs_colour]
            ]
        )
        best_row = np.argmin(np.sum(np.min(means, axis=0), axis=1))
        means = means[:, best_row, :]
        sides = np.argmin(means, axis=0)
        avg_min_dist = np.mean(np.where(sides, means[1], means[0]))

        if avg_min_dist > threshold:
            # print(avg_min_dist)
            hp = 0.0
        else:
            change_point = np.argmin(np.cumsum(2 * sides - 1))
            # print(f'change point: {change_point}')
            hp = change_point / (means.shape[1] - 1)

        return hp
    
    # Calculate each tower's HP
    def calculate_tower_hp(self, image):
        bottom_r = self.calculate_hp(image, br, (68, 151, 231), (59, 73, 107))
        bottom_l = self.calculate_hp(image, bl, (68, 151, 231), (59, 73, 107))
        return [bottom_r, bottom_l]
    
    # Somehow store global timer
    def get_time(self):
        return 1
    
    # Return list of numbers: [elixir, br, bl, time]
    def run(self, image):
        return [self.calculate_elixir(image)] + self.calculate_tower_hp(image) + [self.get_time()]