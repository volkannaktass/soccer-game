import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("PONG")
gameDisplay = pygame.display.set_mode((800,600))



white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,100,0)
blue = (0, 128, 255)
gray = (224, 224, 224)


y1 = 250
y2 = 250

scoreLeft = 0
scoreRight = 0

myfont = pygame.font.SysFont("monospace",40,bold=True)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if y1 >= 0:
            y1 -= 0.5
    if keys[pygame.K_s]:
        if y1 <= 475:
            y1 += 0.5
    if keys[pygame.K_UP]:
        if y2 >= 0:
            y2 -= 0.5
    if keys[pygame.K_DOWN]:
        if y2 <= 475:
            y2 += 0.5

    gameDisplay.fill(green)

    pygame.draw.line(gameDisplay, black, (400, 0), (400, 600), 3)
    pygame.draw.line(gameDisplay, gray, (0, 0), (0, 600), 8)
    pygame.draw.line(gameDisplay, gray, (800, 0), (800, 600), 12)
    pygame.draw.circle(gameDisplay, black, (400, 300), 150, 3)
    pygame.draw.rect(gameDisplay, blue, (40, y1, 10, 125))  # x, y, width, height
    pygame.draw.circle(gameDisplay, white, (400, 300), 8)  # (x, y), radius
    pygame.draw.rect(gameDisplay, red, (750, y2, 10, 125))


    cx = (gameDisplay.get_width() / 2)-59
    cy = (gameDisplay.get_height() - 590)
    scoretext = myfont.render("{0} - {0}".format(scoreLeft,scoreRight), 1, gray)
    #lengthScore = len(scoretext) / 2
    gameDisplay.blit(scoretext,(cx, cy))


    pygame.display.update()

pygame.quit()
