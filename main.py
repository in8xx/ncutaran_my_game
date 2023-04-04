# File created by Nathan Cutaran

# import libs
import pygame as pg
import os

# import settings 
from settings import *

# from pg.sprite import Sprite
from sprites import *

'''
GOAL: Add when above y = 0, more variety of platforms made
'''


# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file
class Game:
    def __init__(self):
        # instantiates the game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(GAME_FONT)
        print(self.screen)

    def new(self):
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORMS_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,10):
            m = Mob(20,20,(RANDCOLOR2))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        # Updates the Game Loop
        self.all_sprites.update()
        # checks if player collides with a platform; only whilst falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits: 
                if hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

        # checks if player is at the top 4th of the screen
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        # checks if the player is below the screen and if true, then playing is false
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        # loop for platforms that randomizes size and position
        while len(self.platforms) < 4:
                width = randint(50, 100)
                height = randint(10, 20) 
                if height < 1:
                    height = 1
                p = Platform(randint(0, WIDTH - width),randint(-40, -30), width, height, RANDCOLOR, 'normal')
                self.platforms.add(p)
                self.all_sprites.add(p)

    # method for recieving the user input
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    # method for drawinf the game, calls upon other methods
    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 20, BLACK, 15, 5)
        pg.display.flip()

    # method for drawing the score on the top left
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiates the game class...
g = Game()


# kick off the game loop
while g.running:
    g.new()
  

pg.quit()

