import pygame
pygame.font.init()
from game import constants
from game.info_text import Setup
from game.stages import Stage

class Redraw_window:
    def __init__(self):
        self.setup = Setup()
        self.stage =Stage()
        
    def variables_window(self,lives,level,score):
        self.__lives = lives
        self.__level = level
        self.__score = score
        
        
    def get_redraw(self):
        self.main_font = self.setup.get_main_font()
        constants.WIN.blit(constants.BG, (0,0))
        # draw text
        lives_label = self.main_font.render(f"Lives: {self.__lives}", 1, (255,255,255))
        level_label = self.main_font.render(f"Level: {self.__level}", 1, (255,255,255)) 
        score_label = self.main_font.render(f"Score: {self.__score}", 1, (255,255,255)) 

        constants.WIN.blit(lives_label, (10, 10))
        constants.WIN.blit(level_label, (constants.WIDTH - level_label.get_width() - 10, 10))
        constants.WIN.blit(score_label, (10, 40))
        

        
        
        
    
    
