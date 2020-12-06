# images from https://www.flaticon.com/
# date October 24, 2020.
# author Subin Sivadas

import pygame
import random

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
alienImage = pygame.image.load('alien.png')
alienX = random.randint(0, 800)
alienY = random.randint(50, 150)
alienX_change = 0.3
alienY_change = 30


def player(x, y):
    screen.blit(playerImage, (x, y))


def alien(x, y):
    screen.blit(alienImage, (x, y))


def fire_bullet(b):
    b.state = "fire"
    screen.blit(bulletImage, (b.x, b.y))
    #global bullet_state
    #bullet_state = "fire"
   # screen.blit(bulletImage, (x, y))
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
                bullet_list.append(b)
                #fire_bullet(b)
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
    alienX += alienX_change

    # check the alien is within the bounds
    if alienX < 0.0:
        alienX_change = 0.3
        alienY += alienY_change
    elif alienX >= 770:
        alienX_change = -0.3
        alienY += alienY_change

    # fire bullet
    for b in bullet_list:
        if b.state == "fire":
            fire_bullet(b)
            # add movement to bullet
            b.y -= bulletY_change
    #if bullet_state == "fire":
    #    fire_bullet(bulletX, bulletY)
    #    bulletY -= bulletY_change

    # place the player and aliens on screen
    player(int(playerX), int(playerY))
    alien(int(alienX), int(alienY))

    # update the screen at the 
    # end of the main game loop
    pygame.display.update()
