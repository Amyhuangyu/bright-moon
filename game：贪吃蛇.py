# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:48:28 2019

@author: huangyu_Amy
"""

import pygame
from pygame.locals import *
import collections
import random
import numpy as np
from sys import exit
pygame.init()
window = pygame.display.set_mode([500,500])
pygame.display.set_caption('贪吃蛇')
screen_width,screen_height = 500,500
SCOPE_X = (0,screen_width - 1)
SCOPE_Y = (0,screen_height - 1)
scope_y = np.arange(2,SCOPE_Y[1])
snake = collections.deque()
def initial(snake):
    snake.clear()
    snake.append((10,scope_y[0]*10))
    snake.append((20,scope_y[0]*10))
    snake.append((30,scope_y[0]*10))
    return snake
snake = initial(snake)
def create_food(snake):
    food_x = random.randint(SCOPE_X[0],SCOPE_X[1])
    food_y = random.randint(SCOPE_Y[0],SCOPE_Y[1])
    while (food_x,food_y) in snake:
        food_x = random.randint(SCOPE_X[0],SCOPE_X[1])
        food_y = random.randint(SCOPE_Y[0],SCOPE_Y[1])
    return food_x,food_y
food = create_food(snake)
pos = [10,0]
while True:
    window.fill((0,255,0))
    pygame.draw.rect(window,(255,0,0),[snake[0][0],snake[0][1],snake[-1][0]-snake[0][0],10])
    pygame.draw.rect(window,(255,0,0),[food[0],food[1],10,10])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else :
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w,pygame.K_UP):
                    if pos[0]:
                        pos[1]=snake[-1][1]-10
                        pos[0]=0
                elif event.key in (pygame.K_s,pygame.K_DOWN):
                    if pos[0]:
                        pos[1]=snake[-1][1]+10
                        pos[0]=0
                elif event.key in (pygame.K_a,pygame.K_LEFT):
                    if pos[1]:
                        pos[0]=snake[-1][0]-10
                        pos[1]=0
                elif event.key in (pygame.K_d,pygame.K_RIGHT):
                    if pos[1]:
                        pos[0]=snake[-1][0]+10
                        pos[1]=0
    next_s = (snake[-1][0]+pos[0],snake[-1][1]+pos[1])
    if next_s == food:
        snake.append(next_s)
        food = create_food(snake)
    else:
        if SCOPE_X[0] <= next_s[0] <= SCOPE_X[1] and SCOPE_Y[0] <= next_s[1] <= SCOPE_Y[1] and next_s not in snake:
            snake.append(next_s)
            del snake[0]
        else:
            print('GAME OVER!')
            snake = initial(snake)
            