# File created by Nathan Cutaran
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries

# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame as pg
import random
import os
# import settings 
from settings import *
from sprites import *
# from pygame.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)


# init pygame and create window
pg.init()
# init sound mixer
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My first game...")
clock = pg.time.Clock() 

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player()

all_sprites.add(player)
player.pos = (0,0)

# creats a forloop four 20 mobs, random sizes 
for i in range(0, 20):
    # imstantiates mobs
    m = Mob([randint(30,90)], [randint(30,90)], [randint(0,255), randint(0,255), randint(0,255)])
    enemies.add(m)
    all_sprites.add(m)
    
# all_sprites.add(testSprite)


# game loop

# as long as the loop is true, it will run forever
while RUNNING:
    #  keep loop running at the right speed
    clock.tick(FPS)
    ### process input events section of game loop
    for event in pg.event.get():
        # check for window closing
        if event.type == pg.QUIT:
            RUNNING = False
            # break
    # print(get_mouse_now())
    ### update section of game loop (if updates take longer the 1/30th of a second, you will get laaaaag...)
    all_sprites.update()
        

    # if a player sprite and an enemy sprite collide then...
    blocks_hit_list = pg.sprite.spritecollide(player, enemies, False)


    # Goes through a list of things
    for block in blocks_hit_list:
        SCORE += 1
        print(SCORE)
        pass
        
    
    # draw and render section of game loop
    screen.fill(BABYBLUE)
    enemies.draw(screen)
    all_sprites.draw(screen)
    draw_text('Score ' + str(SCORE), 22, WHITE, WIDTH/2, WIDTH/10)
    # double buffering draws frames for entire screen
    pg.display.flip()
    # pygame.display.update() -> only updates a portion of the screen
# ends program when loops evaluates to false
pg.quit()

    
