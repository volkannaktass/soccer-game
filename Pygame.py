import pygame
import sys
from pygame.locals import *

WIDTH = 800
HEIGHT = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,100,0)

x1 = 40
y1 = 250
x2 = 750
y2 = 250
rect_width = 10
rect_height = 125
x_circle = 400
y_circle = 300
radius = 8

#scoreLeft = 0
#scoreRight = 0



pygame.init()
pygame.display.set_caption("PONG")
gameDisplay  = pygame.display.set_mode((WIDTH,HEIGHT))


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

    pygame.draw.rect(gameDisplay, black, (x1, y1, rect_width, rect_height))  # x, y, width, height
    pygame.draw.circle(gameDisplay, white, (x_circle, y_circle), radius)  # (x, y), radius
    pygame.draw.rect(gameDisplay, black, (x1, y2, rect_width, rect_height))

    cx = (gameDisplay.get_width() / 2)-50
    cy = (gameDisplay.get_height() - 590)
    scoretext = myfont.render("{0} - {0}".format(scoreLeft,scoreRight), 1, black)
    #lengthScore = len(scoretext) / 2
    gameDisplay.blit(scoretext,(cx, cy))

    
    pygame.display.update()
    
pygame.quit()
