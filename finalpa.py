import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Game")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 발판
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 30
paddle_speed = 10

# 공
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2 - 50
ball_speed_x = 5
ball_speed_y = -5

# 벽돌
brick_width = 75
brick_height = 20
bricks = []
for i in range(6):
    for j in range(8):
        brick_x = 20 + j * (brick_width + 10)
        brick_y = 20 + i * (brick_height + 10)
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # 화면 그리기
    # 배경 화면 -> 검은색
    screen.fill(BLACK)  
    
    # 발판 추가
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))  

    # 공 추가
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    # 벽돌을 그린다
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)  

    pygame.display.flip()  # 화면 업데이트

    # 60프레임 유지
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
