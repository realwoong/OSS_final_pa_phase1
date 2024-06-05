# ball.py
import pygame
from setting import screen_width, screen_height

class Ball:
    def __init__(self):
        self.radius = 7
        self.x = screen_width // 2
        self.y = screen_height // 2 - 50
        self.speed_x = 0
        self.speed_y = 0
        self.piercing = False
