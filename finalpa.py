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
ball_speed_y = 0

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
paused = False  # 추가: 일시정지 상태 변수
lives = 3  # 초기 라이프 설정

# 시간 초기화
start_ticks = pygame.time.get_ticks()

# 시작 버튼 설정
button_color = BLUE
button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 50, 300, 100)
button_text = font.render("Game Start", True, WHITE)
button_text_rect = button_text.get_rect(center=button_rect.center)

# 추가: 메뉴 옵션 버튼 설정
reset_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 50, 300, 50)
resume_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 10, 300, 50)
reset_button_text = small_font.render("Restart Game", True, WHITE)
resume_button_text = small_font.render("Resume Game", True, WHITE)
reset_button_text_rect = reset_button_text.get_rect(center=reset_button_rect.center)
resume_button_text_rect = resume_button_text.get_rect(center=resume_button_rect.center)

# 추가: Game Over 화면의 Restart 버튼 설정
game_over_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 50, 300, 50)
game_over_button_text = small_font.render("Restart Game", True, WHITE)
game_over_button_text_rect = game_over_button_text.get_rect(center=game_over_button_rect.center)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 추가: ESC 버튼으로 메뉴 옵션 열기 및 일시정지
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
                game_active = not paused
        if event.type == pygame.MOUSEBUTTONDOWN:
            if paused:
                if reset_button_rect.collidepoint(event.pos):
                    # RESET 버튼을 누르면 게임 초기화
                    game_active = False
                    game_over = False
                    round_clear = False
                    paused = False
                    lives = 3
                    ball_x = screen_width // 2
                    ball_y = paddle_y - ball_radius
                    ball_speed_x = 0
                    ball_speed_y = 0
                    start_ticks = pygame.time.get_ticks()  # 시간 초기화
                    bricks = []
                    for i in range(6):
                        for j in range(8):
                            brick_x = 20 + j * (brick_width + 10)
                            brick_y = 20 + i * (brick_height + 10)
                            bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))
                elif resume_button_rect.collidepoint(event.pos):
                    # RESUME 버튼을 누르면 게임 이어하기
                    paused = False
                    game_active = True
            elif game_over and game_over_button_rect.collidepoint(event.pos):
                # Game Over 화면에서 Restart 버튼을 누르면 게임 초기화
                game_active = False
                game_over = False
                round_clear = False
                paused = False
                lives = 3
                ball_x = screen_width // 2
                ball_y = paddle_y - ball_radius
                ball_speed_x = 0
                ball_speed_y = 0
                start_ticks = pygame.time.get_ticks()  # 시간 초기화
                bricks = []
                for i in range(6):
                    for j in range(8):
                        brick_x = 20 + j * (brick_width + 10)
                        brick_y = 20 + i * (brick_height + 10)
                        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))
            elif button_rect.collidepoint(event.pos) and not game_over:
                game_active = True
                game_over = False
                round_clear = False
                ball_x = screen_width // 2
                ball_y = paddle_y - ball_radius
                ball_speed_x = 0
                ball_speed_y = 0
                start_ticks = pygame.time.get_ticks()  # 시간 초기화
        if event.type == pygame.KEYDOWN:
            if game_active and ball_speed_y == 0:
                if event.key == pygame.K_SPACE:
                    ball_speed_y = 5
                    ball_speed_x = 0

    # 화면 그리기
    screen.fill(BLACK)  # 배경 화면 -> 검은색

    if game_active and not game_over and not round_clear and not paused:
        # 키보드 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += paddle_speed

        if ball_speed_y == 0:
            ball_x = paddle_x + paddle_width // 2

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

        # 추가: 공이 바닥에 닿으면 라이프 감소
        if ball_y + ball_radius >= screen_height:
            lives -= 1
            if lives <= 0:
                game_active = False
                game_over = True
            else:
                ball_x = paddle_x + paddle_width // 2
                ball_y = paddle_y - ball_radius
                ball_speed_x = 0
                ball_speed_y = 0

        # 벽돌을 모두 제거했을 때 라운드 클리어
        if not bricks:
            game_active = False
            round_clear = True

        # 발판 추가
        pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

        # 공 추가
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

        # 벽돌 추가
        for brick in bricks:
            pygame.draw.rect(screen, WHITE, brick)

        # 경과 시간 계산 및 표시
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        time_text = small_font.render(f"Time: {seconds}", True, WHITE)
        screen.blit(time_text, (screen_width - 100, 40))
    else:
        if game_over:
            text = font.render("Game Over", True, RED)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2 - 50))
            # Game Over 화면에 Restart 버튼 추가
            pygame.draw.rect(screen, BLUE, game_over_button_rect)
            screen.blit(game_over_button_text, game_over_button_text_rect)
            # 최종 시간 표시
            final_time_text = font.render(f"Time: {seconds} seconds", True, RED)
            screen.blit(final_time_text, (screen_width // 2 - final_time_text.get_width() // 2, screen_height // 2 - final_time_text.get_height() // 2 + 20))
        elif round_clear:
            text = font.render("Round Clear", True, RED)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2 - 50))
            # 최종 시간 표시
            final_time_text = font.render(f"Time: {seconds} seconds", True, RED)
            screen.blit(final_time_text, (screen_width // 2 - final_time_text.get_width() // 2, screen_height // 2 - final_time_text.get_height() // 2 + 20))
        elif paused:  # 추가: 일시정지 메뉴 표시
            pygame.draw.rect(screen, BLUE, reset_button_rect)
            pygame.draw.rect(screen, BLUE, resume_button_rect)
            screen.blit(reset_button_text, reset_button_text_rect)
            screen.blit(resume_button_text, resume_button_text_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)
            screen.blit(button_text, button_text_rect)

    # 라이프 표시
    for i in range(lives):
        screen.blit(heart_image, (screen_width - 92 + i * 25, 10))  # 오른쪽 상단에 하트 이미지 추가

    if game_active and ball_speed_y == 0 and not game_over and not round_clear and not paused:
        press_space_text = small_font.render("Press Space", True, WHITE)
        screen.blit(press_space_text, (screen_width // 2 - press_space_text.get_width() // 2, screen_height // 2 + 50))

    pygame.display.flip()  # 화면 업데이트

    # 60프레임 유지
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
