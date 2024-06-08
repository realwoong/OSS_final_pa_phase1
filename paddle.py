# paddle.py
import pygame
from setting import BLUE, screen_width, screen_height

class Paddle:
    def __init__(self):
        self.default_width = 100
        self.width = self.default_width
        self.height = 10
        self.x = (screen_width - self.width) // 2
        ########################### PHASE 2 ##############################
        self.default_y = screen_height - 30
        self.y = self.default_y
        self.default_speed = 10
        self.speed = self.default_speed
        self.speed_up_active = False
        self.speed_up_end_time = 0
        self.up_active = False
        self.up_end_time = 0
        ########################### PHASE 2 ##############################
        self.color = BLUE
        self.gun_active = False
        self.long_active = False
        self.long_end_time = 0
