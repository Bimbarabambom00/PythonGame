import pygame,sys
import os
import random
import time
from pygame.locals import *

screenWidth = 1280
screenHeight= 720

surface = pygame.display.set_mode((screenWidth,screenHeight))
surface.fill((55,55,55))
pygame.display.set_caption("Game Python Construction")

red = (138,7,7)
green = (124, 252, 0)

class playerSprite:
    position_left = 200
    position_top = 200
    width = 50
    height = 50
    keyApressed = False
    keySpressed = False
    keyDpressed = False
    keyWpressed = False
    movement = 2
    mainMovement = 2


def drawBackground():
    surface.fill((55,55,55))

def playerUpdate(x):
    surface.fill((55,55,55))
    pygame.draw.rect(surface, red, pygame.Rect(x.position_left, x.position_top, x.width, x.height),  3) 
    pygame.draw.line(surface,green,((x.position_left+(x.width/2)),(x.position_top+(x.height/2))), (pygame.mouse.get_pos()))
playerUpdate(playerSprite())



while True:
    playerUpdate(playerSprite())
    # LEFT [ A ]
    if  playerSprite.keyApressed == True:
        playerSprite.movement = playerSprite.mainMovement
        if playerSprite.position_left < 1:
            playerSprite.movement = 0
        playerSprite.position_left -= playerSprite.movement
        time.sleep(0.01)
        drawBackground()
        playerUpdate(playerSprite())

    #RIGHT [ D ]
    if  playerSprite.keyDpressed == True:
        playerSprite.movement = playerSprite.mainMovement
        if playerSprite.position_left > (screenWidth - (playerSprite.width + 1)):
            playerSprite.movement = 0
        playerSprite.position_left += playerSprite.movement
        time.sleep(0.01)
        drawBackground()
        playerUpdate(playerSprite())

    #UP [ W ]
    if  playerSprite.keyWpressed == True:
        playerSprite.movement = playerSprite.mainMovement
        if playerSprite.position_top < 1:
            playerSprite.movement = 0
        playerSprite.position_top -= playerSprite.movement
        time.sleep(0.01)
        drawBackground()
        playerUpdate(playerSprite())

    #DOWN [ S ]
    if  playerSprite.keySpressed == True:
        playerSprite.movement = playerSprite.mainMovement
        if playerSprite.position_top > (screenHeight - (playerSprite.height + 1)):
            playerSprite.movement = 0
        playerSprite.position_top += playerSprite.movement
        time.sleep(0.01)
        drawBackground()
        playerUpdate(playerSprite())

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == 97:
                # print("puszczono A")
                playerSprite.keyApressed = False
            if event.key == 100:
                # print("puszczono D")
                playerSprite.keyDpressed = False
            if event.key == 115:
                # print("puszczono A")
                playerSprite.keySpressed = False
            if event.key == 119:
                # print("puszczono D")
                playerSprite.keyWpressed = False


        if event.type == pygame.KEYDOWN:
            os.system('cls')
            # print(event.key)
            drawBackground()
            playerUpdate(playerSprite())
            if event.key == 97:
                # print("← LEFT_A")
                #LEFT
                
                playerSprite.keyApressed = True

                #/LEFT
            if event.key == 100:
                #print("→ RIGHT_D")
                #RIGHT

                playerSprite.keyDpressed = True

                #/RIGHT
            if event.key == 115:
                # print("↓ DOWN_S")
                #DOWN

                playerSprite.keySpressed = True

                #/DOWN
            if event.key == 119:
                # print("↑ UP_W")
                #UP
                
                playerSprite.keyWpressed = True

                #/UP
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()