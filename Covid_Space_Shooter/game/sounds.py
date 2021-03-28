import pygame
import os
from pygame import mixer
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent


def get_shoot_sound():
    bullet_Sound = mixer.Sound(os.path.join("assets", "laser.wav"))
    return bullet_Sound.play()
    
def get_collition_sound():
    damage = mixer.Sound(os.path.join("assets", "damage.wav"))
    return damage.play()
    
def get_pop_enemy_sound():
    pop_Sound = mixer.Sound(os.path.join("assets", "pop.wav"))
    return pop_Sound.play()