from constants import elixir_pixels
from constants import cy1, cy2, cx1, cx2, cx3, cx4, cx5, cx6, cx7, cx8
from constants import br, bl, tr, tl
import cv2
import utils

class GamescreenAligner:
    
    def __init__(self, gamescreen):
        self.gamescreen = gamescreen
    
    def align(self):
        # elixir pixels
        for point in elixir_pixels:
            cv2.circle(self.gamescreen, point, radius=3, color=(0, 0, 255), thickness=-1)
        
        # card boxes
        cv2.rectangle(self.gamescreen, (cx1, cy1), (cx2, cy2), (0, 0, 255), thickness=3)
        cv2.rectangle(self.gamescreen, (cx3, cy1), (cx4, cy2), (0, 0, 255), thickness=3)
        cv2.rectangle(self.gamescreen, (cx5, cy1), (cx6, cy2), (0, 0, 255), thickness=3)
        cv2.rectangle(self.gamescreen, (cx7, cy1), (cx8, cy2), (0, 0, 255), thickness=3)

        # tower health bars
        cv2.rectangle(self.gamescreen, (br[0], br[1]), (br[2], br[3]), (0, 0, 255), thickness=1)
        cv2.rectangle(self.gamescreen, (bl[0], bl[1]), (bl[2], bl[3]), (0, 0, 255), thickness=1)
        cv2.rectangle(self.gamescreen, (tr[0], tr[1]), (tr[2], tr[3]), (255, 0, 0), thickness=1)
        cv2.rectangle(self.gamescreen, (tl[0], tl[1]), (tl[2], tl[3]), (255, 0, 0), thickness=1)

        # display image
        cv2.imshow('marked up image', self.gamescreen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Testing
if __name__ == "__main__":
    # Load a sample gamescreen image
    gamescreen = cv2.imread('data/gamescreen1.png')
    
    # Create an instance of GamescreenAligner and align the gamescreen
    ga = GamescreenAligner(gamescreen)
    ga.align()