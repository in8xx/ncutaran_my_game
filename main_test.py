  # def update(self):
    #     # Update Game Loop
    #     self.all_sprites.update()
    #     # checks if player collides with a platform; only whilst falling
    #     if self.player.vel.y > 0:
    #         hits = pg.sprite.spritecollide(self.player, self.platforms, False)
    #         if hits:
    #             if hits[0].variant == "disappearing":
    #                 hits[0].kill()
    #             elif hits[0].variant == "bouncey":
    #                 self.player.pos.y = hits[0].rect.top
    #                 self.player.vel.y = -PLAYER_JUMP
    #             else:
    #                 self.player.pos.y = hits[0].rect.top
    #                 self.player.vel.y = 0

    #         if self.player.rect.top <= HEIGHT/4:
    #             self.player.pos.y += abs(self.player.vel.y)
    #             for plat in self.platforms:
    #                 plat.rect.y += abs(self.player.vel.y)
    #                 if plat.rect.top >= HEIGHT:
    #                     plat.kill()
    #                     self.score += 5

    #         if self.player.rect.bottom > HEIGHT:
    #             for sprite in self.all_sprites:
    #                 sprite.rect.y -= max(self.player.vel.y, 10)
    #                 if sprite.rect.bottom < 0:
    #                     sprite.kill()
    #         if len(self.platforms) == 0:
    #             self.playing = False

    #         while len(self.platforms) < 6:
    #                 width = randint(50, 100)
    #                 height = 30 - round(self.score/10)
    #                 if height < 1:
    #                     height = 1
    #                 p = Platform(randint(0, WIDTH - width),randint(-75, -30), width, height, (200,200,200), 'normal')
    #                 self.platforms.add(p)
    #                 self.all_sprites.add(p)

def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        # if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        # Die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        # spawn new platforms to keep same average number
        while len(self.platforms) < 6:
                width = randint(50, 100)
                height = 30 - round(self.score/10)
                if height < 1:
                    height = 1
                p = Platform(randint(0, WIDTH - width),randint(-75, -30), width, height, (200,200,200), 'normal')
                self.platforms.add(p)
                self.all_sprites.add(p)