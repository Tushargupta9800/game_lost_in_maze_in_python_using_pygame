################################################################################
#                           by - Tushar Gupta                                  #
#                      Made in python using pygame                             #
################################################################################


#importing lybraries and other files
import pygame
pygame.init()
vec = pygame.math.Vector2

#creating window
width = 1024
height = 640
#16*10
fps = 60
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lost in Maze")
clock = pygame.time.Clock()

#colors
GREEN = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

#importing images
#player
player_img = pygame.image.load("img/player.png")
player_img = pygame.transform.scale(player_img, (64, 64))
player_min_img = pygame.transform.scale(player_img, (50, 50))

#enemy
enemy_img = pygame.image.load("img/enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (55, 55))
enemy_min_img = pygame.transform.scale(enemy_img, (50, 50))

#brick
brick_img = pygame.image.load("img/brick.png")
brick_img = pygame.transform.scale(brick_img, (64, 64))

#bullet
bullet_img = pygame.image.load("img/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (15, 15))

#powerups
#star
star_img = pygame.image.load("img/star.png")
star_img = pygame.transform.scale(star_img, (55, 55))

#med
med_img = pygame.image.load("img/med.png")
med_img = pygame.transform.scale(med_img, (55, 55))

#importing sounds
shoot_snd = pygame.mixer.Sound("snd/shootsnd.wav")
pain_snd = [pygame.mixer.Sound("snd/pain1.wav"),pygame.mixer.Sound("snd/pain2.wav"),pygame.mixer.Sound("snd/pain3.wav"),pygame.mixer.Sound("snd/pain4.wav"),pygame.mixer.Sound("snd/pain5.wav"),pygame.mixer.Sound("snd/pain6.wav"),pygame.mixer.Sound("snd/pain7.wav")]
powerup_snd = pygame.mixer.Sound("snd/power.wav")
pygame.mixer.music.load("snd/bk_music.ogg")
pygame.mixer.music.play(loops = -1)

#making sprites
all_sprites  = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy = pygame.sprite.Group()
bricks = pygame.sprite.Group()
powerups = pygame.sprite.Group()

#some settings
#tile
tilesize = 64
dt = 10

#player
player_health = 100
player_speed = 10
player_rot_speed = 200
player_impulse = 200
player_hit_rect = pygame.Rect(0,0,35,35)

#bullet
bullet_speed = 10
bullet_lifetime = 1000
bullet_rate = 200
diversion = 10
bullet_damage = 10
gun_pos = vec(34, 14)

#enemy
enemy_speed = 4
enemy_hit_rect = pygame.Rect(0, 0, 30, 30)
enemy_health = 100
enemy_damage = 10
enemy_impulse = 20


###test
##win.fill((255, 255, 0))
##win.blit(player_img, (4*tile_width, 4*tile_height))
##win.blit(enemy_img, (2*tile_width, 8*tile_height))
##win.blit(brick_img, (12*tile_width, 3*tile_height))
##win.blit(bullet_img, (8*tile_width, 5*tile_height))
##pygame.display.update()
                     
