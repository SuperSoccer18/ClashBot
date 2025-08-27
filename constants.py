import os
from namespaces import *
import numpy as np

# standard video size
HEIGHT = 1292
WIDTH = 592

# elixir pixels
elixir = np.arange(1, 11)
elixir_pixels = [(int(550 - 40*(10-e)), 1245) for e in elixir]  # x, y format

# card boxes
cy1, cy2 = 1090, 1210
cx1, cx2, cx3, cx4, cx5, cx6, cx7, cx8 = 130, 230, 245, 345, 355, 455, 470, 570

# hog 2.6 cards
hog_2_6_cards = [Cards.HOG_RIDER,
         Cards.ICE_GOLEM,
         Cards.ICE_SPIRIT,
         Cards.FIREBALL,
         Cards.MUSKETEER,
         Cards.THE_LOG,
         Cards.CANNON,
         Cards.SKELETONS]

# tower health bars
br = (446, 812, 518, 814)
bl = (91, 812, 165, 814)
tr = (446, 248, 518, 250)
tl = (91, 248, 165, 250)

# paths
SRC_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(SRC_DIR, 'data')
MODELS_DIR = os.path.join(SRC_DIR, 'models')

# detector units
DETECTOR_UNITS = [
    Units.ARCHER,
    Units.ARCHER_QUEEN,
    Units.BALLOON,
    Units.BANDIT,
    Units.BARBARIAN,
    Units.BARBARIAN_HUT,
    Units.BAT,
    Units.BATTLE_HEALER,
    Units.BATTLE_RAM,
    Units.BOMB_TOWER,
    Units.BOMBER,
    Units.BOWLER,
    Units.BRAWLER,
    Units.CANNON,
    Units.CANNON_CART,
    Units.DARK_PRINCE,
    Units.DART_GOBLIN,
    Units.ELECTRO_DRAGON,
    Units.ELECTRO_GIANT,
    Units.ELECTRO_SPIRIT,
    Units.ELECTRO_WIZARD,
    Units.ELITE_BARBARIAN,
    Units.ELIXIR_COLLECTOR,
    Units.ELIXIR_GOLEM_LARGE,
    Units.ELIXIR_GOLEM_MEDIUM,
    Units.ELIXIR_GOLEM_SMALL,
    Units.EXECUTIONER,
    Units.FIRE_SPIRIT,
    Units.FIRE_CRACKER,
    Units.FISHERMAN,
    Units.FLYING_MACHINE,
    Units.FURNACE,
    Units.GIANT,
    Units.GIANT_SKELETON,
    Units.GIANT_SNOWBALL,
    Units.GOBLIN,
    Units.GOBLIN_CAGE,
    Units.GOBLIN_DRILL,
    Units.GOBLIN_HUT,
    Units.GOLDEN_KNIGHT,
    Units.GOLEM,
    Units.GOLEMITE,
    Units.GUARD,
    Units.HEAL_SPIRIT,
    Units.HOG,
    Units.HOG_RIDER,
    Units.BABY_DRAGON,
    Units.HUNTER,
    Units.ICE_GOLEM,
    Units.ICE_SPIRIT,
    Units.ICE_WIZARD,
    Units.INFERNO_DRAGON,
    Units.INFERNO_TOWER,
    Units.KNIGHT,
    Units.LAVA_HOUND,
    Units.LAVA_PUP,
    Units.LITTLE_PRINCE,
    Units.LUMBERJACK,
    Units.MAGIC_ARCHER,
    Units.MEGA_KNIGHT,
    Units.MEGA_MINION,
    Units.MIGHTY_MINER,
    Units.MINER,
    Units.MINION,
    Units.MINIPEKKA,
    Units.MONK,
    Units.MORTAR,
    Units.MOTHER_WITCH,
    Units.MUSKETEER,
    Units.NIGHT_WITCH,
    Units.PEKKA,
    Units.PHOENIX_EGG,
    Units.PHOENIX_LARGE,
    Units.PHOENIX_SMALL,
    Units.PRINCE,
    Units.PRINCESS,
    Units.RAM_RIDER,
    Units.RASCAL_BOY,
    Units.RASCAL_GIRL,
    Units.ROYAL_GHOST,
    Units.ROYAL_GIANT,
    Units.ROYAL_GUARDIAN,
    Units.ROYAL_HOG,
    Units.ROYAL_RECRUIT,
    Units.SKELETON,
    Units.SKELETON_DRAGON,
    Units.SKELETON_KING,
    Units.SPARKY,
    Units.SPEAR_GOBLIN,
    Units.TESLA,
    Units.TOMBSTONE,
    Units.VALKYRIE,
    Units.WALL_BREAKER,
    Units.WITCH,
    Units.WIZARD,
    Units.X_BOW,
    Units.ZAPPY,
]
