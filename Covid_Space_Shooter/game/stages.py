
from game import constants
from game.sprites import Player, Enemy
import random

class Stage():
    
    def __init__(self):
        self.enemies = []
        self.wave_length = 5
        
    def get_new_enemy(self):
        for enemy in self.enemies:
                enemy.draw(constants.WIN)
                
    def get_more_enemies(self):
        self.wave_length += 5
        for i in range(self.wave_length):
            enemy = Enemy(random.randrange(50, constants.WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
            self.enemies.append(enemy)
                    
    def get_enemies(self):
        return self.enemies
    
   
        