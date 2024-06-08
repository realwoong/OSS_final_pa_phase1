import pygame
import random

class Brick(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 75, 20)

def get_stage_1_bricks():
    return [Brick(20 + j * 85, 20 + i * 30) for i in range(6) for j in range(8)]

def get_stage_2_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if (i + j) % 2 == 0:
                bricks.append(Brick(20 + j * 85, 20 + i * 30))
    return bricks

def get_stage_3_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if i % 2 == 0:
                bricks.append(Brick(20 + j * 85, 20 + i * 30))
            else:
                bricks.append(Brick(20 + j * 85 + 42, 20 + i * 30))
    return bricks

def get_stage_4_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if (i * j) % 3 != 0:
                bricks.append(Brick(20 + j * 85, 20 + i * 30))
    return bricks

##################################################################
########################### PHASE 2 ##############################
##################################################################
def get_stage_time_attack_bricks():
    bricks= []
    for i in range(6):
        for j in range(8):
            if random.random() > 0.7:
                bricks.append(Brick(20 + j * 85, 20 + i * 30))
    return bricks
##################################################################
########################### PHASE 2 ##############################
##################################################################