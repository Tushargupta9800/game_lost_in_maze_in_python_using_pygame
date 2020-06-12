################################################################################
#                           by - Tushar Gupta                                  #
#                      Made in python using pygame                             #
################################################################################


#importing lybraries and other files
import pygame
pygame.init()
from Resources.sprites import*
from Resources.setandvar import* 
from Resources.define import*

count = 0
class Game():
    def __init__ (self):
        self.total = 275
        pygame.display.update()
        self.map = Map("map/level1.txt")
        self.dt = 1
        
    def update(self):
        win.fill(BROWN)
        self.camera.update(self.player)
        all_sprites.update()

        for sprite in all_sprites:
            if isinstance(sprite, Enemy):
                sprite.draw_health()
            win.blit(sprite.image, self.camera.apply(sprite))
        writeonscreen(str(game.total))
        drawhealth(self.player.health)

        pygame.display.update()
    def get_events(self):

        if self.player.health <= 0:
            self.gameover(self.total)

        if self.total == 0:
            self.gameover_screen()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        

    def new(self):
        count =0 
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Brick(self, col, row)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):            
                if tile == 'E': 
                    count += 1
                    Enemy(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'M':
                    Powerup(self, col, row, 1)
                if tile == 'S':
                    Powerup(self, col, row, 2)
        self.camera = Camera(self.map.width, self.map.height)
        print(count)

    def collision(self):
        
        if self.player.power == 1:
            if pygame.time.get_ticks() - self.player.power_time >= 30000:
                self.player.power = 0
            hits = pygame.sprite.groupcollide(enemy, bullets, True, True)
            for hit in hits:
                self.total -= 1
        else:
            hits = pygame.sprite.groupcollide(enemy, bullets, False, True)
        for i in hits:
            i.health -= 10
            if i.localvel:
                i.localvel = 0
                i.vel += 10*i.vel

        hits = pygame.sprite.groupcollide(bullets, bricks, True, False)
        hits = pygame.sprite.spritecollide(self.player, enemy, False, collide_hit_rect)
        for hit in hits:
            random.choice(pain_snd).play()
            self.player.health -= 0.2
            if hit.localvel:
                hit.localvel = 0
                hit.vel += 10*hit.vel

        hits = pygame.sprite.spritecollide(self.player, powerups, True)
        for hit in hits:
            powerup_snd.play()
            if hit.image == star_img:
                self.player.power = 1
                self.player.power_time = pygame.time.get_ticks()
            if hit.image == med_img:
                self.player.health += 10
                if self.player.health > 100:
                    self.player.health = 100
    def gameover_screen(self):
        wait = True
        while wait:
            win.fill(BROWN)
            write_on_screen("Lost In Maze", width/2, 50, 100)
            write_on_screen("---- A Tile Based Game ----", width/2, 120, 30)
            write_on_screen("----Made in Python using pygame ----", width/2, 150, 30)
            write_on_screen("Congratulations:", width/2, 220, 50)
            write_on_screen("You kill all the zombies", width/2, 280, 40)
            write_on_screen("Now you can escape through the secret door", width/2, 325, 40)
            write_on_screen("Press Escape button on your keyboard to escape through that door", width/2, 370, 40)
            write_on_screen("By- Tushar Gupta", width - 100, height - 20, 30)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
    def gameover(self, score):
         wait = True
         while wait:
            win.fill(BROWN)
            write_on_screen("Lost In Maze", width/2, 50, 100)
            write_on_screen("---- A Tile Based Game ----", width/2, 120, 30)
            write_on_screen("----Made in Python using pygame ----", width/2, 150, 30)
            write_on_screen("OOPS! You Lose:", width/2, 220, 50)
            write_on_screen("You failed to kill all the zombies", width/2, 280, 40)
            write_on_screen("Now you can't escape through the secret door", width/2, 325, 40)
            write_on_screen("But you can Press Escape button on your", width/2, 370, 40)
            write_on_screen("keyboard to escape through that door", width/2, 415, 40)
            write_on_screen("By- Tushar Gupta", width - 100, height - 20, 30)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

run = True
start_screen()
game = Game()
game.gameover_screen()
game.new()
while run:
    clock.tick(fps)
    game.collision()
    game.update()
    game.get_events()
