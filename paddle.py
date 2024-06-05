# paddle.py
import pygame
from setting import BLUE, screen_width, screen_height

class Paddle:
    def __init__(self):
        self.default_width = 100
        self.width = self.default_width
        self.height = 10
        self.x = (screen_width - self.width) // 2
        self.y = screen_height - 30
        self.speed = 10
        self.color = BLUE
        self.gun_active = False
        self.long_active = False
        self.long_end_time = 0
