# File created by Nathan Cutaran

# import libs
import pygame as pg
import os

# import settings 
from settings import *

# from pg.sprite import Sprite
from sprites import *

'''
GOAL 1 :Add mobs that collides with player
GOAL 2: Add a score
GOAL 3: Add platforms when plaver < y = 0, 
'''


# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

pg.init()
screen = pg.display.set_mode((700, 500))

# defines the button perameters, boarder, font, size etc...
def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pg.font.SysFont("Cascadia Code", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pg.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pg.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pg.draw.rect(screen, bg, (x, y, w , h))
    return screen.blit(text_render, (x, y)) 

def menu():
    pg.display.set_caption("menu")
    # creates what is displayed on the buttons
    b0 = button(screen, (10, 10), "Do you wanna play Jumper?", 72, "white on black")
    b1 = button(screen, (150, 300), "Na", 60, "red on blue")
    b2 = button(screen, (450, 300), "Let's play", 60, "purple on green")

    # loop of the menu
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # quits pygame
                if b1.collidepoint(pg.mouse.get_pos()):
                    pg.quit()
                elif b2.collidepoint(pg.mouse.get_pos()):
                    g.new()
        pg.display.update()
    pg.quit()

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

    # method that starts a new game
    def new(self):
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORMS_LIST:
            # calls the variable "p", in the mob class
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,10):
            # calls the variable "m", the mob class
            m = Mob(20,20,(RED))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()

    # method that has the game loop
    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            # calls upon the methods listed below
            self.events()
            self.update()
            self.draw()

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

    # method for drawing the game

    # draws background, sprites, and text
    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 20, BLACK, 15, 5)
        pg.display.flip()

    '''
    GOAL 2: Score
    '''
    # method for drawing the score on the top left
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)   

    '''
    Goal 1: Collisions between Mob and Player
    Requires 2 questions to be asked
    1) What happens when the mob collides with the play? (Player position moves)
    2) What will happen when the mob hits the player from a certain side? '
    (M hits P @ Top -> P goes Down, M hits P @ Down -> P goes Up, M hits P @ Left -> P goes Right, M hits P @ Right -> P goes Left )
    '''
    
    # method that updates the results of player's position 
    def update(self):
        # Updates the the sprites in the game loop
        self.all_sprites.update()
        
        # variable for when the mob hits the plater
        mhits = pg.sprite.spritecollide(self.player, self.enemies, False)
        # when mob hits...
        if mhits:
            # mob hits player on the left, then the moves 10 pixels to right
            if self.player.vel.x < 0:
                self.player.pos.x += 10
            
            # mob hits player on the right, then  moves player 10 pixels to the left
            if self.player.vel.x > 0:
                self.player.pos.x -= 10
            # mob hits player from bottom, then moves player 10 pixels up

            if self.player.vel.y > 0:
                self.player.pos.y -= 10

            # mob hits player from the top, then moves player 10 pixels doen
            if self.player.vel.y < 0:
                self.player.pos.y += 10

        
            
        # checks if player collides with a platform
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits: 
                if hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

        '''
        Goal 2: Make more platforms as the player moves up
        Requires a variety of steps
        1) Verifying that the player is in the right position so that the platforms can be created
        2) 



        '''
        # checks if player is at the top 4th of the screen to verify that the randomized platforms can be generated
        # The platforms move cohesively with the player's velocity
        # Once the platform is greater that the height (the bottom of the screen) by the player moving up, the platform will disappear (score goes up)
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

         # creats a falling effect, freezes all the sprites(platforms, mob, player)
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()

        # if the sprite falls the platforms will hit the top of the screen and their height will equal zero stopping the game loop
        if len(self.platforms) == 0:
            self.playing = False

        # loop for returning the platforms to the screen after it is verifyied the the player is at the top fourth of the screen
        while len(self.platforms) < 4:
                width = 50
                height = 10 
                if height < 1:
                    height = 1
                # the first two values make it possible for the player to jump to the new platforms as these arguements define the position
                p = Platform(randint(0, WIDTH - width), randint(-2, -1), width, height, BABYBLUE, 'normal')
                self.platforms.add(p)
                self.all_sprites.add(p)
                            
# instantiates the game class
g = Game()


# starts game loop
while g.running:
    menu()
    g.new()

  

pg.quit()

