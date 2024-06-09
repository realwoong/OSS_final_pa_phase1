import pygame
import random

####################
#####phase2 - 1#####
####################
class Brick(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 75, 20)
        self.health = random.randint(1, 5)
        self.font = pygame.font.Font(None, 24)
    def block_collide(self):
        self.health -= 1
        return self.health <= 0
    def render_health(self, surface):
        health_text = self.font.render(str(self.health), True, pygame.Color('black'))
        text_rect = health_text.get_rect(center=self.center)
        surface.blit(health_text, text_rect)
####################
#####phase2 - 1#####
####################
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
