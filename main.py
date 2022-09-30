import pygame,sys
import os
from pygame.locals import *
surface = pygame.display.set_mode((1280,720))
surface.fill((55,55,55))
pygame.display.set_caption("Game Python")

class PlayerSprite:
    position_left = 0
    position_top = 0
    width = 40
    height = 40

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            os.system('cls')
            print(event.key)
            if event.key == 97:
                print("← LEFT_A")
            if event.key == 100:
                print("→ RIGHT_D")
            if event.key == 115:
                print("↓ DOWN_S")
            if event.key == 119:
                print("↑ UP_W")
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()