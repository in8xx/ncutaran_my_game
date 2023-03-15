# File created by Nathan Cutaran

import pygame as pg

from pygame.sprite import Sprite

from random import randint

# * imports everything from other file
from settings import *

vec = pg.math.Vector2

# player class

# class is CAPITALIZED
# self refers to the instance of the class

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False

    def input(self):
        keystate = pg.key.get_pressed()

        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
    
    # this is a method that keeps it on screen
    def inbounds(self):
        if self.rect.x > WIDTH - 50:
            self.pos.x = WIDTH - 25
            self.pos.x = 0

        if self.rect.x < 0:
            self.pos.x = WIDTH + 25
            self.vel.x = 0
          
        if self.rect.y < 0:
            self.pos.y = HEIGHT - 25
            self.pos.y = 0
  
        if self.rect.y > HEIGHT:
    
            self.pos.y = HEIGHT - 25
            self.pos.y = 0

    def update(self):        
        self.inbounds()
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos


class Mob(Sprite):
    def __init__(self, width, height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((80,80))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01

    # def inbounds(self):
    #     if self.rect.x > WIDTH - 50:
    #         # self.pos.x = WIDTH - 25
    #         self.vel.x *= -1 
    #         # print("i am off the right side of the screen...")
    #     if self.rect.x < 0:
    #         self.vel.x *= -1
    #         # print("i am off the left side of the screen...")
    #     if self.rect.y > HEIGHT:
    #         self.vel.y *= -1
    #         # print("i am off the bottom of the screen")
    #     if self.rect.y < 0:
    #         self.vel.y *=1
    #         # print("i am off the top of the screen...")

    # def behavior(self):
    #     # acc go up
    #     self.acc.y = -MOB_ACC
    #     # self.acc.x = -MOB_ACC 
    #     # self.acc.y = MOB_ACC
    #     # self.acc.x = MOB_ACC
    #     if self.rect.x > WIDTH:
    #         print("I'm off the right screen...")
    #     if self.rect.x < 0:
    #         print("I'm off the left screen...")
    #     if self.rect.y < 0:
    #         print("I'm off the top screen...")
    #         # reduces vel
    #         self.vel *= -1
    #         self.acc *= -1
    #         self.pos.y <= 0
    #     if self.rect.y > HEIGHT:
    #         print("I'm off the bottom screen...")

    # def update(self):
    #     # self.inbounds()
        
    #     self.acc = self.vel * MOB_FRICTION
    #     self.vel += self.acc
    #     self.behavior()
    #     self.pos += self.vel + 0.5 * self.acc
    #     self.rect.center = self.pos

    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    def update(self):
        self.inbounds()
        self.pos += self.vel
        self.rect.center = self.pos