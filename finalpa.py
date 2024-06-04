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

# 폰트 설정
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# 하트 이미지 로드
heart_image = pygame.image.load('images/heart.png')
heart_image = pygame.transform.scale(heart_image, (20, 20))  # 하트 이미지 크기 조정

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
ball_speed_x = 0
ball_speed_y = 5

# 벽돌
brick_width = 75
brick_height = 20
bricks = []
for i in range(6):
    for j in range(8):
        brick_x = 20 + j * (brick_width + 10)
        brick_y = 20 + i * (brick_height + 10)
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# 게임 상태
game_active = False
game_over = False
round_clear = False
lives = 3  # 초기 라이프 설정

# 시작 버튼 설정
button_color = BLUE
button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 50, 300, 100)
button_text = font.render("Game Start", True, WHITE)
button_text_rect = button_text.get_rect(center=button_rect.center)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and not game_over:
                game_active = True
                game_over = False
                round_clear = False

    # 화면 그리기
    screen.fill(BLACK)  # 배경 화면 -> 검은색

    if game_active and not game_over and not round_clear:
        # 키보드 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += paddle_speed

        # 공의 위치 업데이트
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # 공이 화면 경계에 부딪히면 방향 전환
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
            ball_speed_x = -ball_speed_x
        if ball_y - ball_radius <= 0:
            ball_speed_y = -ball_speed_y

        # 공이 패들에 부딪히면 방향 전환
        if paddle_y < ball_y + ball_radius < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
            ball_speed_y = -ball_speed_y
            # 공이 패들의 왼쪽에 맞으면 왼쪽으로, 오른쪽에 맞으면 오른쪽으로 튕겨나감
            hit_pos = ball_x - paddle_x  # 패들에 맞은 위치
            ball_speed_x = (hit_pos - paddle_width / 2) / (paddle_width / 2) * 5  # 속도 조정

        # 공이 벽돌에 부딪히면 벽돌 제거 및 방향 전환
        for brick in bricks[:]:
            if brick.collidepoint(ball_x, ball_y):
                bricks.remove(brick)
                ball_speed_y = -ball_speed_y
                break

        # 공이 바닥에 닿으면 게임 오버
        if ball_y + ball_radius >= screen_height:
            game_active = False
            game_over = True

        # 벽돌을 모두 제거했을 때 라운드 클리어
        if not bricks:
            game_active = False
            round_clear = True

        # 발판 추가
        pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

        # 공 추가
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

        # 벽돌을 그린다
        for brick in bricks:
            pygame.draw.rect(screen, WHITE, brick)
    else:
        if game_over:
            text = font.render("Game Over", True, RED)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        elif round_clear:
            text = font.render("Round Clear", True, RED)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        else:
            pygame.draw.rect(screen, button_color, button_rect)
            screen.blit(button_text, button_text_rect)

    # 라이프 표시
    for i in range(lives):
        screen.blit(heart_image, (screen_width - 92 + i * 25, 10))  # 오른쪽 상단에 하트 이미지 추가

    pygame.display.flip()  # 화면 업데이트

    # 60프레임 유지
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
