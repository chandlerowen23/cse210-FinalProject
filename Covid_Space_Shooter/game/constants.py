import pygame
from pygame import mixer
import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent


pygame.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Covid-19 Space Battle")

 # Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "cov.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "cov.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "cov.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "bernie.png"))

# Lasers
RED_LASER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "red_laser.png")), (40,40))
GREEN_LASER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "green_laser.png")), (40,40))
BLUE_LASER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "blue_laser.png")), (40,40))
# Bernie mask
Mask = pygame.transform.scale(pygame.image.load(os.path.join("assets", "mask.png")), (40,40))
Syringe = pygame.transform.scale(pygame.image.load(os.path.join("assets", "syringe.png")), (50,50))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

#Colors
White = (255,255,255)


# Background Sound
mixer.music.load(os.path.join("assets", "background.wav"))
mixer.music.play(-1)
