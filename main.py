import pygame,sys
from pygame.locals import *
surface = pygame.display.set_mode((1280,720))
surface.fill((55,55,55))
pygame.display.set_caption("Game Construction")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()