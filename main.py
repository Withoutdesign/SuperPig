#-------------------- Chance Lively --------------------#
#----------------- Python Chicken Drop  -----------------#

import sys
import pygame
import random

pygame.init()

#Screen size
width = 800
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)

#Background
background = pygame.image.load("Sky.png")
background = pygame.transform.scale(background, size)

#Window title
pygame.display.set_caption("Pig drop")

coolDown = False
timer = 0

#Sprite
pig = pygame.image.load("Pig.png")
pig = pygame.transform.scale(pig, (86, 68))

iterator = 0
numOfPigs = 5
startX = []
startY = []
speed = []

while iterator < numOfPigs:
    startX.append(random.randint(0, width - pig.get_width() + 1))
    startY.append(0 - random.randint(pig.get_height(), pig.get_height() * 2))
    speed.append(random.random() + float(random.randint(0,3)) + 0.1)
    iterator += 1

replayScreen = False

#Text styles
bigFont = pygame.font.SysFont(None, 200)
playAgainText = bigFont.render("Play Again?", True, (244, 151, 150))
paX = width/2 - playAgainText.get_rect().width/2

#Yes/No texts
smallFont = pygame.font.SysFont(None, 100)
yesText = smallFont.render("YES", True, (244, 151, 150))
yesX = width/4 - yesText.get_rect().width/2
noText = smallFont.render("NO", True, (244, 151, 150))
noX = width - width/4 - yesText.get_rect().width/2

#-------------------- Game Loop --------------------#

gameOver = False

while gameOver == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and coolDown == False:
                pig = pygame.transform.scale(pig, (172, 136))
                coolDown = True
                timer = pygame.time.get_ticks()

    #-------------------- Input Checks --------------------#


    if pygame.mouse.get_pressed()[0]:
        coords = pygame.mouse.get_pos()

        if replayScreen == False:
            iterator = 0
            while iterator < numOfPigs:
                if coords[0] >= startX[iterator] and coords[0] <= startX[iterator] + pig.get_width() and coords[1] >= startY[iterator] and coords[1] <= startY[iterator] + pig.get_height():
                    startX[iterator] = random.randint(0, width - pig.get_width() + 1)
                    startY[iterator] = 0 - random.randint(pig.get_height(), pig.get_height() * 2)
                    speed[iterator] = random.random() + float(random.randint(0,3)) + 0.1
                    break
                iterator += 1

        else:
            #Yes check
            if coords[0] > yesX and coords[0] < yesX + yesText.get_rect().width and coords[1] > 450 and coords[1] < 450 + yesText.get_rect().height:
                iterator = 0
                while iterator < numOfPigs:
                    startX[iterator] = random.randint(0, width - pig.get_width() + 1)
                    startY[iterator] = 0 - random.randint(pig.get_height(), pig.get_height() * 2)
                    speed[iterator] = random.random() + float(random.randint(0,3)) + 0.1
                    iterator += 1
                replayScreen = False

            #No Check
            if coords[0] > noX and coords[0] < noX + noText.get_rect().width and coords[1] > 450 and coords[1] < 450 + noText.get_rect().height:
                gameOver = True

    #-------------------- Updating Info --------------------#

    if replayScreen == False:
        iterator = 0
        while iterator < numOfPigs:
            if startY[iterator] + pig.get_height() > height:
                replayScreen = True
                break
            startY[iterator] += speed[iterator]
            iterator += 1

    #-------------------- Drawing Info --------------------#

    if replayScreen == False:
        screen.blit(background, (0, 0))
        iterator = 0
        while iterator < numOfPigs:
            screen.blit(pig, (startX[iterator], startY[iterator]))
            iterator += 1

        iterator = 0

    else:
        screen.fill((255, 235, 236))

        screen.blit(playAgainText, (paX, 150))
        screen.blit(yesText, (yesX, 450))
        screen.blit(noText, (noX, 450))

    #-------------------- Powerup Info --------------------#

    if coolDown == True:
        #Powerup time 
        if pygame.time.get_ticks() - timer > 2000:
            pig = pygame.transform.scale(pig, (86, 68))
            coolDown = False

    pygame.display.flip()

pygame.display.quit()
