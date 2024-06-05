# maps.py
import pygame

class Brick(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 75, 20)

def get_stage_1_bricks():
    return [Brick(20 + j * 85, 20 + i * 30) for i in range(6) for j in range(8)]

def get_stage_2_bricks():
    return [Brick(20 + j * 85, 20 + i * 30) for i in range(6) for j in range(8)]

def get_stage_3_bricks():
    return [Brick(20 + j * 85, 20 + i * 30) for i in range(6) for j in range(8)]

def get_stage_4_bricks():
    return [Brick(20 + j * 85, 20 + i * 30) for i in range(6) for j in range(8)]
