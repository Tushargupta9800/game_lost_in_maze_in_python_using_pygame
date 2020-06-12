################################################################################
#                           by - Tushar Gupta                                  #
#                      Made in python using pygame                             #
################################################################################


#importing lybraries and other files
import pygame
pygame.init()
from Resources.setandvar import*
from Resources.define import*
import random
vec = pygame.math.Vector2

class Brick(pygame.sprite.Sprite):
        def __init__ (self, game, x, y):
            
            self.groups = all_sprites, bricks
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = brick_img
            self.rect = self.image.get_rect()
            self.pos = vec(x, y) * tilesize + (tilesize/2, tilesize/2)
            self.rect.center = self.pos
        def update(self):
            pass

class Bullet(pygame.sprite.Sprite):
    def __init__ (self, game, pos, rot):
        
        self.groups = all_sprites, bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rot = rot
        self.pos = vec(pos) + gun_pos.rotate(self.rot)
        self.rect.center = self.pos
        self.vel = vec(bullet_speed, 0).rotate(self.rot)
        self.time = pygame.time.get_ticks()

    def update(self):
        self.pos += self.vel*self.game.dt
        self.rect.center = self.pos
        if pygame.time.get_ticks() - self.time >= bullet_lifetime:
            self.kill()

class Powerup(pygame.sprite.Sprite):
        def __init__ (self, game, x, y, text):
            self.groups = all_sprites, powerups
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            if text == 2:
                    self.image = star_img
            else:
                    self.image = med_img
            self.rect = self.image.get_rect()
            self.pos = vec(x, y) * tilesize + (tilesize/2, tilesize/2)
            self.rect.center = self.pos 

        def update(self):
                pass
        

class Enemy(pygame.sprite.Sprite):
        def __init__ (self, game, x, y):
            
            self.groups = all_sprites, enemy
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = enemy_img
            self.rect = self.image.get_rect()
            self.pos = vec(x, y) * tilesize + (tilesize/2, tilesize/2)
            self.rect.center = self.pos
            self.vel = vec(0, 0)
            self.rot = 0
            self.hit_rect = enemy_hit_rect.copy()
            self.health = 100
            self.acc = vec(0, 0)
            self.localvel = 1
            self.x = self.pos.x - 20
            self.y = self.pos.y - 20

        def update(self):
            self.get_rotation()
            old_pos = self.rect.center
            self.image = pygame.transform.rotate(enemy_img, self.rot)
            if (self.game.player.pos - self.pos).magnitude() <= 320:
                    self.acc = vec(enemy_speed, 0).rotate(-self.rot)
                    self.acc += self.vel * -1
                    self.rect = self.image.get_rect()
                    self.rect.center = old_pos
                    self.hit_rect.centerx = self.pos.x
                    collide_with_bricks(self, bricks, 'x')
                    self.hit_rect.centery = self.pos.y
                    collide_with_bricks(self, bricks, 'y')
                    self.rect.center = self.hit_rect.center
                    self.vel = vec(4, 0).rotate(-self.rot)
                    self.localvel = 1
                    self.check_with_others()
                    self.x = self.pos.x - 20
                    self.y = self.pos.y - 20
                    if not self.pos == self.game.player.pos:
                        self.pos += self.vel*self.game.dt + 0.5 * self.acc * self.game.dt ** 2
                        self.rect.center = self.pos

            if self.health <= 0:
                self.kill()
                self.game.total -= 1
            

        def get_rotation(self):
            self.rot = (self.game.player.pos - self.pos).angle_to(vec(random.randint(1, 10), 0))
            
        def check_with_others(self):
            for i in enemy:
                if i == enemy:
                    pass
                else:
                    if (self.pos - i.pos).magnitude() < 50:
                        temp_rot = (self.pos - i.pos).angle_to(vec(random.randint(10, 20), 0))
                        self.vel = self.vel.rotate(temp_rot)

        def draw_health(self):
            if self.health > 60:
                col = GREEN
            elif self.health > 30:
                col = YELLOW
            else:
                col = RED
            width = int(self.rect.width * self.health / 100)
            self.health_bar = pygame.Rect(0, 0, width, 7)
            if self.health < 100:
                pygame.draw.rect(self.image, col, self.health_bar)
        
class Player(pygame.sprite.Sprite):
        def __init__ (self, game, x, y):
            
            self.groups = all_sprites
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = player_img
            self.rect = self.image.get_rect()
            self.pos = vec(x, y) * tilesize + (tilesize/2, tilesize/2)
            self.rect.center = self.pos
            self.vel = vec(0,0)
            self.rot = 0
            self.hit_rect = player_hit_rect
            self.bullet_time = pygame.time.get_ticks()
            self.health = 100
            self.power = 0
            self.power_time = pygame.time.get_ticks()

        def update(self):
            self.get_keys()
            self.pos = self.pos + self.vel
            self.rect.center = self.pos
            self.vel = vec(0, 0)
            old_pos = self.rect.center
            self.image = pygame.transform.rotate(player_img, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = old_pos
            self.hit_rect.centerx = self.pos.x
            collide_with_bricks(self, bricks, 'x')
            self.hit_rect.centery = self.pos.y
            collide_with_bricks(self, bricks, 'y')
            self.rect.center = self.hit_rect.center

        def get_keys(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_UP]:
                self.vel = vec(player_speed , 0).rotate(-self.rot)
            if key[pygame.K_DOWN]:
                self.vel = vec(-player_speed , 0).rotate(-self.rot)
            if key[pygame.K_RIGHT]:
                self.rot -= 5
                self.rot %= 360
            if key[pygame.K_LEFT]:
                self.rot += 5
                self.rot %= 360
            if key[pygame.K_SPACE]:
                if pygame.time.get_ticks() - self.bullet_time >= bullet_rate:
                    shoot_snd.play()
                    self.game.bullet = Bullet(self.game, self.pos, -self.rot)
                    self.bullet_time = pygame.time.get_ticks()
                
            

        
