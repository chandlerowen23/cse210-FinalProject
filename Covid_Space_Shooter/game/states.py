import pygame
import os
import time
import random
from pygame import mixer
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent
pygame.font.init()
from game import constants
from game.sprites import Player, Enemy

class States: 


    def collide(self, obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    def main(self):
        run = True
        FPS = 60
        level = 0
        lives = 3
        main_font = pygame.font.SysFont("comicsans", 50)
        lost_font = pygame.font.SysFont("comicsans", 60)

        enemies = []
        wave_length = 5
        enemy_vel = 1

        player_vel = 5
        laser_vel = 5

        player = Player(300, 630)

        clock = pygame.time.Clock()

        lost = False

        def redraw_window():
            constants.WIN.blit(constants.BG, (0,0))
            # draw text
            lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
            level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

            constants.WIN.blit(lives_label, (10, 10))
            constants.WIN.blit(level_label, (constants.WIDTH - level_label.get_width() - 10, 10))

            for enemy in enemies:
                enemy.draw(constants.WIN)

            player.draw(constants.WIN)

            if lost:
                lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
                constants.WIN.blit(lost_label, (constants.WIDTH/2 - lost_label.get_width()/2, 350))
                

            pygame.display.update()

        while run:
            clock.tick(FPS)
            redraw_window()

            if player.health <= 0 and lives >= 1:
                lives -= 1
                player.health = 100
            
            if lives <= 0:
                lost = True
                lives = 0


            if len(enemies) == 0:
                level += 1
                wave_length += 5
                for i in range(wave_length):
                    enemy = Enemy(random.randrange(50, constants.WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                    enemies.append(enemy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.x - player_vel > 0: # left
                player.x -= player_vel
            if keys[pygame.K_d] and player.x + player_vel + player.get_width() < constants.WIDTH: # right
                player.x += player_vel
            if keys[pygame.K_w] and player.y - player_vel > 0: # up
                player.y -= player_vel
            if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < constants.HEIGHT: # down
                player.y += player_vel
            if keys[pygame.K_SPACE]:
                player.shoot()
                bullet_Sound = mixer.Sound(os.path.join("assets", "laser.wav"))
                bullet_Sound.play()

            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)

                if random.randrange(0, 2*60) == 1:
                    enemy.shoot()

                if self.collide(enemy, player):
                    player.health -= 10
                    enemies.remove(enemy)
                elif enemy.y + enemy.get_height() > constants.HEIGHT:
                    lives -= 1
                    enemies.remove(enemy)

            player.move_lasers(-laser_vel, enemies)

    def info_menu(self):
        title_font = pygame.font.SysFont("comicsans", 50)
        text_font = pygame.font.SysFont("comicsans", 30)
        run = True
        while run:
            constants.WIN.blit(constants.BG, (0,0))
            title_label = title_font.render("Instructions", 1, constants.White)
            constants.WIN.blit(title_label, (constants.WIDTH/2 - title_label.get_width()/2, 100))
            text_label1 = text_font.render("You suddenly find yourself in space and reincarnated as...", 1, constants.White)
            constants.WIN.blit(text_label1, (constants.WIDTH/2 - text_label1.get_width()/2, 250))
            text_label2 = text_font.render("Bernie Sanders!", 1, constants.White)
            constants.WIN.blit(text_label2, (constants.WIDTH/2 - text_label2.get_width()/2, 280))
            text_label3 = text_font.render("You have a mission to prevent the spead of covid-19 throughout the galaxy!", 1, constants.White)
            constants.WIN.blit(text_label3, (constants.WIDTH/2 - text_label3.get_width()/2, 310))
            text_label4 = text_font.render("Difficulty will increase with levels and covid-19 cells shoot back at YOU!", 1, constants.White)
            constants.WIN.blit(text_label4, (constants.WIDTH/2 - text_label4.get_width()/2, 340))
            text_label5 = text_font.render("Will you rise to the challenge?", 1, constants.White)
            constants.WIN.blit(text_label5, (constants.WIDTH/2 - text_label5.get_width()/2, 370))
            text_label6 = text_font.render("Movement: W = Up, A = Left, S = Down, D = Right, Space = Shoot", 1, constants.White)
            constants.WIN.blit(text_label6, (constants.WIDTH/2 - text_label6.get_width()/2, 400))
            exit_label = text_font.render("Press the Mouse to return to menu..", 1, constants.White)
            constants.WIN.blit(exit_label, (constants.WIDTH/2 - exit_label.get_width()/2, 650))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
        
    # def game_over(self):
    #     title_font = pygame.font.SysFont("Comicsans", 50)
    #     text_font = pygame.font.SysFont("comicsans",30)
    #     run = True
    #     while run:
    #         constants.WIN.blit(constants.BG, (0,00))
    #         title_label = title_font.render("Game Over", 1, constants.Red)
    #         constants.WIN.blit(title_label, (constants.WIDTH/2 - title_label.get_width()/2, 100))
    #         text_label = text_font.render("Would you like to play again? (Enter)", 1, constants.White)
    #         constants.WIN.blit(text_label, (constants.WIDTH/2 - text_label.get_WIDTH()/2, 250))
    #         text_label1 = text_font.render("Press the mouse to return to menu..", 1, constants.White)
    #         constants.WIN.Blit(text_label1, (constants.WIDTH/2 - text_label.get_width()/2, 650))
    #         pygame.display.update()
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 run = False
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 States.main()




