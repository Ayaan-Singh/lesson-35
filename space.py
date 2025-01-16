import pygame
import math
import random

sw = 800
sh = 600
psx = 370
psy = 380
esym = 50
esxma = 150
esx = 4
esy = 40
bsy = 10
cd = 27

pygame.init()
screen=pygame.display.set_mode((sw, sh))
background = pygame.image.load('th(39).jpeg')
pygame.display.set_caption('space invaders')
playerimg = pygame.image.load('spaceship.png')
playerx = psx
playery = psy
playerxc = 0

enemyimg = []
enemyx = []
enemyy = []
enemyxc = []
enemyyc = []
num = 6
for i in range(num):
    enemyimg.append(pygame.image.load('ufo.png'))
    enemyx.append(random.randint(0, sw - esym))
    enemyy.append(random.randint(50, 150))
    enemyxc.append(esx)
    enemyyc.append(esy)
bulletimg = pygame.image.load('bullet(1).png')
bulletx = 0
bullety = psy
bxc = 0 
bulletyc = bsy
bs = 'ready'
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10
overfont = pygame.font.Font('freesansbold.ttf', 64)
def ss():
    scoret = font.render('score: ' + str(score), True, (255, 255, 255))
    screen.blit(scoret, (textx, texty))
def gameend():
    over = overfont.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over, (200, 250))
def player(x, y):
    screen.blit(playerimg, (x, y))
def enemy (x, y, i):
    screen.blit(enemyimg[i], (x, y))
def bullet(x, y):
    global bs
    bs = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))
def iscollision(ex, ey, bx, by):
    distance = math.sqrt((ex - bx) ** 2 + (ey - by) ** 2)
    return distance < cd

