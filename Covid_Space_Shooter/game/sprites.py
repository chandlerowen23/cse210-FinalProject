
import pygame
from game import constants
import random
import os
from pygame import mixer
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

class Laser:
        def __init__(self, x, y, img):
            self.x = x
            self.y = y
            self.img = img
            self.mask = pygame.mask.from_surface(self.img)
        
        def collide(self, obj1, obj2):
            offset_x = obj2.x - obj1.x
            offset_y = obj2.y - obj1.y
            return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

        def draw(self, window):
            window.blit(self.img, (self.x, self.y))

        def move(self, vel):
            self.y += vel

        def off_screen(self, height):
            return not(self.y <= height and self.y >= 0)

        def collision(self, obj):
            return self.collide(self, obj)


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(constants.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
                damage = mixer.Sound(os.path.join("assets", "damage.wav"))
                damage.play()

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = constants.YELLOW_SPACE_SHIP
        self.laser_img = constants.Mask
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.collision_enemy = 0

    def move_lasers(self, vel, objs):
        self.cooldown()
        self.throw_random()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(constants.HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.collision_enemy += 1
                        print('COLLITION')
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                            
    def get_collision_enemy(self):
        return self.collision_enemy

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
    
    def throw_random(self):
        x = random.randint(0,11)
        if x % 2 == 0:
            self.laser_img = constants.Syringe
        else:
            self.laser_img = constants.Mask

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


class Enemy(Ship):
    COLOR_MAP = {
                "red": (constants.RED_SPACE_SHIP, constants.RED_LASER),
                "green": (constants.GREEN_SPACE_SHIP, constants.GREEN_LASER),
                "blue": (constants.BLUE_SPACE_SHIP, constants.BLUE_LASER)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1