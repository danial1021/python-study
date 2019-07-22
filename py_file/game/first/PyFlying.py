__author__ = 'samsjang@naver.com'

import pygame #PyGame 라이브러리를 import 
import shutil
import time


#흰색 표현값, 게임판의 높낮이
WHITE = (255,255,255)
pad_width = 1024
pad_height = 512
background_width = 1024

def back(background,x,y):
    global gamepad
    gamepad.blit(background, (x,y))


def airplane(x,y): # 비행기 위치 좌표
    global gamepad, aircraft
    gamepad.blit(aircraft, (x,y))


def runGame(): # initGame함수에서 호출함
    global gamepad, aircraft, clock, background1, background2 # 전역변수로 사용 및 초기화함

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0 # y축으로 비행기 이동변수 및 초기 위치 변수

    background1_x = 0
    background2_x = background_width

    crashed = False # 게임종료를 위한 플래그
    while not crashed:
        for event in pygame.event.get(): # 여러 이벤트 리턴
            if event.type == pygame.QUIT: # 마우스로 창을 닫는 이벤트가 아니면 
                crashed = True # 게임판을 흰색으로 채우고 게임판을 다시 그림

            if event.type == pygame.KEYDOWN: # 5픽셀식 움직이도록
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change == 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change == 0

        y += y_change 
        gamepad.fill(WHITE)           

        # 배경 이미지와 배경 이미지 복사본을 왼쪽으로 2픽셀 만큼 이동
        background1_x -= 2
        background2_x -= 2

        # 배경을 지우고 진행방향으로 위치시킴
        if background1_x == -background_width:
          background_x = background_width

        if background2_x == -background_width:
         background2_x = background_width

        back(background1,background1_x,0)
        back(background2,background2_x,0)            

        airplane(x,y)
        pygame.display.update()
        clock.tick(60)

    pygame.quit() # 초기화한 PyGame 종료
    quit()

def initGame(): # 게임 초기화
    global gamepad, aircraft, clock, background1, background2

    pygame.init() # 라이브러리 초기화
    gamepad = pygame.display.set_mode((pad_width, pad_height)) # 판 크리 1024*512
    pygame.display.set_caption('PyFlying') # title
    aircraft = pygame.image.load('plane.png')
    background1 = pygame.image.load('background.png')
    background2 = background1.copy()

    clock = pygame.time.Clock() # FPS설정 - 클락(60)
    runGame() # 게임 구동 


if __name__ == '__main__':
    initGame()    