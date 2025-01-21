import pygame
import math
import random

sw = 800
sh = 600
psx = 370
psy = 380
esym = 50
esyma = 150
esx = 4
esy = 4
bsy = 10
cd = 27

pygame.init()
screen=pygame.display.set_mode((sw, sh))
background = pygame.image.load('th (39).jpeg')
pygame.display.set_caption('space invaders')
playerimg = pygame.image.load('spaceship.png')
playerimg = pygame.transform.scale(playerimg, (34, 34))
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
    enemyimg[i] = pygame.transform.scale(enemyimg[i], (64, 64))
    enemyx.append(random.randint(0, sw - esym))
    enemyy.append(random.randint(50, 150))
    enemyxc.append(esx)
    enemyyc.append(esy)
bulletimg = pygame.image.load('bullet (1).png')
bulletimg = pygame.transform.scale(bulletimg, (15, 15))
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
def ss(textx,texty):
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
    distance_squared = (ex - bx) ** 2 + (ey - by) ** 2
    return distance_squared < cd ** 2

running = True
while running :
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxc -= 5
            if event.key == pygame.K_RIGHT:
                playerxc = 5
            if event.key == pygame.K_SPACE:
                bs = 'ready'
                bulletx = playerx
                bullet(bulletx, bullety)
            if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerxc = 0
    playerx += playerxc
    playerx = max(0,min(playerx, sw - 64))
    for i in range (num):
        if enemyy[i] > 340:
            for j in range(num):
                enemyy[j] = 2000
            gameend()
            break
        enemyx[i] += enemyxc[i]
        if enemyx[i] <= 0 or enemyx[i] >= sw - enemyimg[i].get_width():
            enemyxc[i] *= -1
            enemyy[i] += enemyyc[i]
        if iscollision(enemyx[i], enemyy[i], bulletx + 16, bullety + 10):
            bullety = psy
            bs = 'ready'
            score += 1
            enemyx[i] = random.randint(0, sw - 64)
            enemyy[i] = random.randint(esym, esyma)
        enemy(enemyx[i], enemyy[i], i)
    if bullety <= 0:
        bullety = psy
        bs = 'ready'
    if bs == 'fire':
        bullet(bulletx, bullety)
        bullety -= bulletyc
    player(playerx, playery)
    ss(textx, texty)
    pygame.display.update()



