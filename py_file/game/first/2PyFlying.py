__author__ = 'samsjang@naver.com'

import pygame
import random
from time import sleep

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 512
background_width = 1024
aircraft_width = 90
aircraft_height = 55


bat_width = 110
bat_height = 67

# def back(x,y):
#     global gamepad
#     gamepad.blit(background, (x,y))

# def airplane(x,y):
#     global gamepad, aircraft
#     gamepad.blit(aircraft, (x,y))

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj, (x,y))

def runGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires, bullet, boom

    isShotBat = False
    boom_count = 0

    bullet_xy = []

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background1_x = 0 
    background2_x = background_width

    bat_x = pad_width
    bat_y = random.randrange(0, pad_height)

    fire_x = pad_width
    fire_y = random.randrange(0, pad_height)
    random.shuffle(fires)
    fire = fires[0]

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

                elif event.key == pygame.K_LCTRL:
                    bullet_x = x + aircraft_width
                    bullet_y = y + aircraft_height/2
                    bullet_xy.append([bullet_x,bullet_y])

                # elif event.key == pygame.K_SPACE:
                #     sleep(5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        #Clear gamepad
        gamepad.fill(WHITE)   
        
        #Draw Background
        background1_x -= 2
        background2_x -= 2

        if background1_x == -background_width:
            background1_x = background_width

        if background2_x == -background_width:
            background2_x = background_width 

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)   

        #Aircraft Position
        y += y_change
        if y < 0:
            y = 0
        elif y > pad_height - aircraft_height:
            y = pad_height - aircraft_height

        # Bat Position   
        bat_x -= 7
        if bat_x <= 0:
            bat_x = pad_width
            bat_y = random.randrange(0, pad_height)

        # Fireball Position
        if fire == None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x <= 0:
            fire_x = pad_width
            fire_y = random.randrange(0, pad_height)
            random.shuffle(fires)
            fire = fires[0]    

        # Bullets Position
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0] += 15
                bullet_xy[i][0] = bxy[0]

                # Check if bullet strike Bat
                if bxy[0] > bat_x:
                    if bxy[1] > bat_y and bxy[1] < bat_y + bat_height:
                        bullet_xy.remove(bxy)
                        isShotBat = True 

                if bxy[0] >= pad_width:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass

        drawObject(aircraft, x, y)
    
        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)

        if not isShotBat:
            drawObject(bat, bat_x, bat_y)
        else:
            drawObject(boom, bat_x, bat_y)
            boom_count += 1
            if boom_count > 5:
                boom_count = 0
                bat_x = pad_width
                bat_y = random.randrange(0, pad_height-bat_height)
                isShotBat = False  


        if fire != None:
            drawObject(fire, fire_x, fire_y)                   

        pygame.display.update()
        clock.tick(60) 

        #back(background1, background1_x, 0)
        #back(background2, background2_x, 0)

        #airplane(x,y)
    pygame.quit()
    quit() 


def initGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires, bullet

    fires = []
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('PyFlyig')
    aircraft = pygame.image.load('plane.png')
    background1 = pygame.image.load('background.png')
    background2 = background1.copy()
    bat = pygame.image.load('fireball.png')
    fires.append(pygame.image.load('fireball.png'))
    fires.append(pygame.image.load('fireball2.png'))

    boom = pygame.image.load('boom.png')

    for i in range(3):
        fires.append(None)

    bullet = pygame.image.load('bullet.png')

    clock = pygame.time.Clock()
    runGame()


if __name__ == '__main__':
    initGame()  