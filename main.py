# images from https://www.flaticon.com/
# code from https://www.youtube.com/watch?v=FfWpgLFMI7w&t=5466s&ab_channel=freeCodeCamp.org
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
background = pygame.image.load('background_space.png')

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
class Aliens:
    num = 0
    alien_image = 'alien.png'
    x = 0
    y = 0
    x_change = 0
    y_change = 0
    def __init__(self,number):
        self.num = number

number_of_aliens = 6
alien_list =[]
for i in range(number_of_aliens):
    alien_list.append(Aliens(i))

for alien in alien_list:
    alien.x = random.randint(0, 770)
    alien.y = random.randint(50, 150)
    alien.x_change = 0.3
    alien.y_change = 30
    pygame.image.load(alien.alien_image)

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


def show_alien(alien):
    screen.blit(pygame.image.load(alien.alien_image), (alien.x, alien.y))

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
    for alien in alien_list:
        alien.x += alien.x_change
        if alien.x <0.0:
            alien.x_change = 0.3
            alien.y += alien.y_change
        elif alien.x >= 770:
            alien.x_change = -0.3
            alien.y += alien.y_change
        collision = iscollision(alien.x, alien.y, bullet_list)

        if collision:
            bullet_sound = mixer.Sound('explosion.wav')
            bullet_sound.play()
            score += 1
            alien.x = random.randint(0, 770)
            alien.y = random.randint(50, 150)
        show_alien(alien)
    # add movement to bullets
    for b in bullet_list:
        if b.state == "fire":
            fire_bullet(b)
            b.y -= bulletY_change

    # place the player and aliens on screen
    player(int(playerX), int(playerY))

    show_score(textX,textY)

    # update the screen at the 
    # end of the main game loop
    pygame.display.update()
