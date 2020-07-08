import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,100,0)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(green)
myfont = pygame.font.SysFont("monospace",20)
score = 0

pygame.draw.rect(gameDisplay, black, (30,250,10,125))  #left, top, width, height
pygame.draw.circle(gameDisplay, white, (400,300), 8) #(left, top), radius
pygame.draw.rect(gameDisplay, black, (750,250,10,125))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



    cx = (gameDisplay.get_width() / 2)-120
    #cy = gameDisplay.get_height() / 2
    scoretext = myfont.render("Team A: {0} - {0} Team B".format(score), 1, black)
    #lengthScore = len(scoretext) / 2
    gameDisplay.blit(scoretext,(cx,0))

    
    pygame.display.update()
    
