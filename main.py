# images from https://www.flaticon.com/
# date October 24, 2020.
# author Subin Sivadas
import math
import pygame
import random
from pygame import mixer

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Titled Icon
pygame.display.set_caption("space invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('space.png')

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# bullet
bulletImage = pygame.image.load('love.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10


class Bullet:
    x = 300
    y = 200
    state = "ready"

bullet_list = []

# player image and position
playerImage = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# alien image and position
alienImagelist = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_of_aliens = 6
for i in range(num_of_aliens):
    alienImagelist.append( pygame.image.load('alien.png'))
    alienX.append(random.randint(0, 770))
    alienY.append(random.randint(50, 150))
    alienX_change.append(0.3)
    alienY_change.append(30)
#score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x,y):
    score_display = font.render("score :"+str(score), True, (255, 255, 255))
    screen.blit(score_display, (x, y))
def player(x, y):
    screen.blit(playerImage, (x, y))


def alien(x, y,i):
    screen.blit(alienImagelist[i], (x, y))


def fire_bullet(b):
    b.state = "fire"
    screen.blit(bulletImage, (b.x, b.y))

def iscollision(alienx, alieny, bulletlist):
    crash = False
    for bullet in bullet_list:
        distance = math.sqrt((math.pow(bullet.x-alienx, 2))+(math.pow(bullet.y-alieny, 2)))
        if distance < 25:
            crash = True
            break
    return crash
# Game Loop
running = True
while running:
    # fill the screen with R,G,B value. range 0-255.
    screen.fill((0, 0, 0))
    # add background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # event for pressing close window
        if event.type == pygame.QUIT:
            running = False
    # if keystroke is pressed check if
    # its left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # move left
                playerX_change = -1.0
            if event.key == pygame.K_RIGHT:
                # move right
                playerX_change = 1.0
            if event.key == pygame.K_UP:
                # move up
                playerY_change = -1.0
            if event.key == pygame.K_DOWN:
                # move down
                playerY_change = 1.0
            if event.key == pygame.K_SPACE:
                b = Bullet()
                b.x = playerX
                b.y = playerY
                fire_bullet(b)
                bullet_sound =mixer.Sound('laser.wav')
                bullet_sound.play()
                bullet_list.append(b)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    # add movement to player
    playerX += playerX_change
    playerY += playerY_change

    # check the player is within the bounds
    if playerX > 770.0:
        playerX = 770.0
    if playerX < 0.0:
        playerX = 0.0
    if playerY > 570.0:
        playerY = 570.0
    if playerY < 0.0:
        playerY = 0.0

    # add movement to the alien ship
    for i in range(num_of_aliens):
        alienX[i] += alienX_change[i]
        # check the alien is within the bounds
        if alienX[i] < 0.0:
            alienX_change[i] = 0.3
            alienY[i] += alienY_change[i]
        elif alienX[i] >= 770:
            alienX_change[i] = -0.3
            alienY[i] += alienY_change[i]

        collision = iscollision(alienX[i], alienY[i], bullet_list)

        if collision:
            bullet_sound = mixer.Sound('explosion.wav')
            bullet_sound.play()
            score += 1
            print(score)
            alienX[i] = random.randint(0, 770)
            alienY[i] = random.randint(50, 150)
        alien(int(alienX[i]), int(alienY[i]),i)
    # fire bullet
    for b in bullet_list:
        if b.state == "fire":
            fire_bullet(b)
            # add movement to bullet
            b.y -= bulletY_change

    # place the player and aliens on screen
    player(int(playerX), int(playerY))

    show_score(textX,textY)

    # update the screen at the 
    # end of the main game loop
    pygame.display.update()
