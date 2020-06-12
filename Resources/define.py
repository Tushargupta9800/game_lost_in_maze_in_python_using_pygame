################################################################################
#                           by - Tushar Gupta                                  #
#                      Made in python using pygame                             #
################################################################################


#importing lybraries and other files
import pygame
pygame.init()
from Resources.setandvar import *
vec = pygame.math.Vector2

def write_on_screen(text, x, y, size):
    font = pygame.font.match_font('arial')
    fonter = pygame.font.Font(font, size)
    makesurface = fonter.render(text, True, (255, 255, 255))
    text_rect = makesurface.get_rect()
    text_rect.center = (x, y)
    win.blit(makesurface, text_rect)

def start_screen():
    run = True
    while run:

        win.fill(BROWN)
        write_on_screen("Lost In Maze", width/2, 50, 100)
        write_on_screen("---- A Tile Based Game ----", width/2, 120, 30)
        write_on_screen("----Made in Python using pygame ----", width/2, 150, 30)
        write_on_screen("Controls:", width/2, 230, 50)
        write_on_screen("Use arrow keys to move", width/2, 280, 40)
        write_on_screen("Use Space bar to shoot", width/2, 330, 40)
        write_on_screen("Description:", width/2, 420, 35)
        write_on_screen("You (       ) struct in a maze castle full of       ", width/2, 460, 30)
        write_on_screen("with a gun and the only way out is by killing ", width/2, 500, 30)
        write_on_screen("all the zombies", width/2, 540, 30)
        write_on_screen("Press 'p' to start the game", width/2, 600, 40)
        write_on_screen("By- Tushar Gupta", width - 100, height - 20, 30)
        win.blit(player_min_img, (325, 440))
        win.blit(enemy_min_img, (708, 435))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    run = False
        
        

def writeonscreen(score):
    font = pygame.font.match_font('arial')
    fonter = pygame.font.Font(font, 50)
    makesurface = fonter.render(score, True, (255, 255, 255))
    text_rect = makesurface.get_rect()
    text_rect.center = (width - 50, 30)
    win.blit(makesurface, text_rect)


def drawhealth(health):
    ret = False
    if health <= 0:
        health = 0
        ret = True

    length = 100
    height = 10
    outline = pygame.Rect(10, 10, length, height)
    fill_rect = pygame.Rect(10 , 10, health, height)
    pygame.draw.rect(win, GREEN, fill_rect)
    pygame.draw.rect(win, WHITE, outline, 2)
    return ret

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

def collide_with_bricks(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            #sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            #sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width*tilesize
        self.height = self.tile_height*tilesize


def makelines(w, h):
    for i in range(h):
        pygame.draw.line(win, (0, 0, 0), (0, i*tilesize),
                         (1024*tilesize, i*tilesize))

    for i in range(w):
        pygame.draw.line(win, (0, 0, 0), (i*tilesize, 0),
                         (i*tilesize, 480*tilesize))

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0,0, width, height)
        self.width = width
        self.height  = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, from_this):
        x = -from_this.rect.centerx + int(width/2)
        y = -from_this.rect.centery + int(height/2)

        #adjusting the camera
        x = min(0, x)   #left
        y = min(0, y)   #top
        x = max(-(self.width - width), x)   #right
        y = max(-(self.height - height), y) #bottom
        self.camera = pygame.Rect(x,y, self.width, self.height)
