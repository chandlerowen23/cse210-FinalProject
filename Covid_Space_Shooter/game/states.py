import pygame
import random
pygame.font.init()
from game import constants
from game.sprites import Player, Enemy
from game.stages import Stage
from game.info_text import Setup
from game.collide import Collide
from game import sounds
from game import main


class States: 
    
    def __init__(self):
        self.setup = Setup()
        self.collition = Collide()
        self.stage =Stage()


    def main(self):
        run = True
        lives = 3
        main_font = self.setup.get_main_font()
        enemies = []
        
        enemies = self.stage.get_enemies()
        level = 0
        enemy_vel = 1

        player_vel = 5
        laser_vel = 5
        score = 0

        player = Player(350, 630)

        clock = pygame.time.Clock()

        lost = False

        def redraw_window():
            constants.WIN.blit(constants.BG, (0,0))
            # draw text
            lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
            level_label = main_font.render(f"Level: {level}", 1, (255,255,255)) 
            score_label = main_font.render(f"Score: {score}", 1, (255,255,255)) 

            constants.WIN.blit(lives_label, (10, 10))
            constants.WIN.blit(level_label, (constants.WIDTH - level_label.get_width() - 10, 10))
            constants.WIN.blit(score_label, (10, 40))
          
            #--stages-----
            self.stage.get_new_enemy()
            player.draw(constants.WIN) 

            pygame.display.update()

        while run:
            clock.tick(constants.FPS)
            redraw_window()

            if player.health <= 0 and lives >= 1:
                lives -= 1
                player.health = 100
            
            if lives <= 0:
                lost = True
                lives = 0
                set_level = level

            if lost:
                States.game_over(self)
                if States.game_over(self) == True:
                    self.main()

            if len(enemies) == 0:
                level += 1
                self.stage.get_more_enemies()
                
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
                sounds.get_shoot_sound()
          
            
            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)
                

                if random.randrange(0, 2*60) == 1:
                    enemy.shoot()
                    
                if player.get_collision_enemy() > 0:
                    score = player.get_collision_enemy()
                    

                if self.collition.collide(enemy, player):
                    player.health -= 10
                    enemies.remove(enemy)
                    sounds.get_collition_sound()
                    
                elif enemy.y + enemy.get_height() > constants.HEIGHT:
                    lives -= 1
                    enemies.remove(enemy)
                    

            player.move_lasers(-laser_vel, enemies)
            
 
    def info_menu(self):
        run = True
        while run:
            self.setup.get_instructions()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
        
    def game_over(self):
        run = True
        while run:
            self.setup.game_over_text()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main.main_menu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True




