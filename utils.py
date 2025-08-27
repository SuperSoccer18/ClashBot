import cv2
from PIL import Image
import imagehash
import json
import constants
import numpy as np


# Resize gamescreen to standard size
def resize(gamescreen):
    return cv2.resize(gamescreen, (constants.WIDTH, constants.HEIGHT))

# Display the image in a window
def display_img(image):
    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)   # Wait for any key press
    cv2.destroyAllWindows()

# Display RBG values through clicking
def display_img_pixels(image):
    def show_rgb_helper(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            b, g, r = image[y, x]
            print(f"Clicked at ({x}, {y}): BGR = {b}, {g}, {r}")

    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", show_rgb_helper)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Generate phashes for hog 2.6 cards
def generate_deck_phashes():
    hog_26 = {
        'fireball.jpg': 'Fireball',
        'ice_golem.jpg': 'Ice Golem',
        'ice_spirit.jpg': 'Ice Spirit',
        'musketeer.jpg': 'Musketeer',
        'the_log.jpg': 'Log',
        'hog_rider.jpg': 'Hog Rider',
        'cannon.jpg': 'Cannon',
        'skeletons.jpg': 'Skeletons'
    }

    known_hashes = {}
    for filename, card_name in hog_26.items():
        img = Image.open(f'cards/{filename}')
        phash = imagehash.phash(img)
        known_hashes[card_name] = phash
    known_hashes_str = {card_name: str(phash) for card_name, phash in known_hashes.items()}

    with open("hog26_hashes.json", "w") as f:
        json.dump(known_hashes_str, f)

# Convert image from cv2 format to PIL format
def cv2_to_PIL(cv2_image):
    rgb_img = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb_img)

# Convert image from PIL to cv2 format
def pil_to_cv2(pil_image):
    # Ensure no alpha channel
    if pil_image.mode == "RGBA":
        pil_image = pil_image.convert("RGB")
    elif pil_image.mode == "L":
        # Grayscale, convert to 3-channel grayscale
        pil_image = pil_image.convert("RGB")
    elif pil_image.mode != "RGB":
        pil_image = pil_image.convert("RGB")
    # Convert to numpy array
    np_image = np.array(pil_image)
    # Convert RGB to BGR
    cv2_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)

    return cv2_image

# Convert image coordinate to tile
def get_tile(x, y):
    return None