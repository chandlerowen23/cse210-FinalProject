import pygame
import os
import time
import random
pygame.font.init()

from game.states import States
from game import constants

states = States()

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 50)
    game_name = pygame.font.SysFont("Comicsans", 80)
    run = True 
    while run:
        constants.WIN.blit(constants.BG, (0,0))
        title_label = game_name.render("COVID-19 Bernie Defense", 1, (225,0,0))
        constants.WIN.blit(title_label, (constants.WIDTH/2 - title_label.get_width()/2, 150))
        start_label = title_font.render("Press the mouse to begin", 1, constants.White)
        info_label = title_font.render("Press enter for Instruction", 1, constants.White)
        constants.WIN.blit(start_label, (constants.WIDTH/2 - start_label.get_width()/2, 300))
        constants.WIN.blit(info_label, (constants.WIDTH/2 - info_label.get_width()/2, 400))
        exit_label = title_font.render("Press Q to Quit", 1, constants.White)
        constants.WIN.blit(exit_label, (constants.WIDTH/2 - exit_label.get_width()/2, 600))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
               states.main()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                   states.info_menu()
                if event.key == pygame.K_q:
                    run = False
    pygame.quit()



