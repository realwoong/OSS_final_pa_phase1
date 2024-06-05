# game_state.py
import pygame
import random
from paddle import Paddle
from ball import Ball
from setting import item_images, screen_width, screen_height, BLUE, PURPLE

class GameState:
    def __init__(self):
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = []
        self.items = []
        self.lives = 3
        self.start_ticks = pygame.time.get_ticks()
        self.paused_ticks = 0
        self.game_active = False
        self.game_over = False
        self.round_clear = False
        self.paused = False
        self.stage_select = True  # 스테이지 선택 상태 추가
        self.item_drop_chance = 0.3
        self.item_types = list(item_images.keys())
        self.final_time = 0  # final_time 변수 추가
        self.stage = 1  # stage 변수 추가
