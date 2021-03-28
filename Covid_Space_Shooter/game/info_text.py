
import pygame
from game import constants

class Setup():
    def __init__(self):
        self.title_font = pygame.font.SysFont("comicsans", 50)
        self.text_font = pygame.font.SysFont("comicsans", 30)
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.lost_font = pygame.font.SysFont("comicsans", 60)

    def get_instructions(self): 
        
        constants.WIN.blit(constants.BG, (0,0))
        title_label = self.title_font.render("Instructions", 1, constants.White)
        constants.WIN.blit(title_label, (constants.WIDTH/2 - title_label.get_width()/2, 100))
        text_label1 = self.text_font.render("You suddenly find yourself in space and reincarnated as...", 1, constants.White)
        constants.WIN.blit(text_label1, (constants.WIDTH/2 - text_label1.get_width()/2, 250))
        text_label2 = self.text_font.render("Bernie Sanders!", 1, constants.White)
        constants.WIN.blit(text_label2, (constants.WIDTH/2 - text_label2.get_width()/2, 280))
        text_label3 = self.text_font.render("You have a mission to prevent the spead of covid-19 throughout the galaxy!", 1, constants.White)
        constants.WIN.blit(text_label3, (constants.WIDTH/2 - text_label3.get_width()/2, 310))
        text_label4 = self.text_font.render("Difficulty will increase with levels and covid-19 cells shoot back at YOU!", 1, constants.White)
        constants.WIN.blit(text_label4, (constants.WIDTH/2 - text_label4.get_width()/2, 340))
        text_label5 = self.text_font.render("Will you rise to the challenge?", 1, constants.White)
        constants.WIN.blit(text_label5, (constants.WIDTH/2 - text_label5.get_width()/2, 370))
        text_label6 = self.text_font.render("Movement: W = Up, A = Left, S = Down, D = Right, Space = Shoot", 1, constants.White)
        constants.WIN.blit(text_label6, (constants.WIDTH/2 - text_label6.get_width()/2, 400))
        exit_label = self.text_font.render("Press the Mouse to return to menu..", 1, constants.White)
        constants.WIN.blit(exit_label, (constants.WIDTH/2 - exit_label.get_width()/2, 650))
        pygame.display.update() 
        
    def game_over_text(self):
        constants.WIN.blit(constants.BG, (0,00))
        title_label = self.title_font.render("Game Over", 1, constants.Red)
        constants.WIN.blit(title_label, (constants.WIDTH/2 - title_label.get_width()/2, 100))
        text_label = self.text_font.render("Would you like to play again? (Enter)", 1, constants.White)
        constants.WIN.blit(text_label, (constants.WIDTH/2 - text_label.get_width()/2, 250))
        text_label1 = self.text_font.render("Press the mouse to return to menu..", 1, constants.White)
        constants.WIN.blit(text_label1, (constants.WIDTH/2 - text_label.get_width()/2, 650))
        pygame.display.update()
    
    def get_main_font(self):
        return self.main_font
    
    def get_lost_font(self):
        return self.lost_font
    
