import pygame
import sys
import random
from maps import get_stage_1_bricks, get_stage_2_bricks, get_stage_3_bricks, get_stage_4_bricks, Brick

pygame.init() # 초기화 이후 import
from paddle import Paddle
from ball import Ball
from game_state import GameState

from setting import screen_width, screen_height, screen, WHITE, BLACK, RED, BLUE, PURPLE, font, small_font, tiny_font, heart_image, item_images
from button import reset_button_rect, resume_button_rect, reset_button_text, resume_button_text_rect, next_round_button_rect, start_menu_button_rect, next_round_button_text, start_menu_button_text, next_round_button_text_rect, start_menu_button_text_rect, game_over_button_rect, game_over_button_text, game_over_button_text_rect, button_color, button_rect, button_text, button_text_rect, stage_1_button_rect, stage_2_button_rect, stage_3_button_rect, stage_4_button_rect, stage_1_button_text, stage_2_button_text, stage_3_button_text, stage_4_button_text, stage_1_button_text_rect, stage_2_button_text_rect, stage_3_button_text_rect, stage_4_button_text_rect

# 게임 상태 클래스
game_state = GameState()

# 이벤트 처리 함수
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and game_state.game_active:
                while len(game_state.bricks) > 1:
                    game_state.bricks.pop()
            if event.key == pygame.K_ESCAPE:
                game_state.paused = not game_state.paused
                game_state.game_active = not game_state.paused
                if game_state.paused:
                    game_state.paused_ticks = pygame.time.get_ticks()
                else:
                    game_state.start_ticks += pygame.time.get_ticks() - game_state.paused_ticks
            if game_state.game_active and game_state.ball.speed_y == 0:
                if event.key == pygame.K_SPACE:
                    game_state.ball.speed_y = 5
                    game_state.ball.speed_x = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(event.pos)

# 마우스 클릭 처리 함수
def handle_mouse_click(pos):
    if game_state.paused:
        if reset_button_rect.collidepoint(pos):
            reset_game()
        elif resume_button_rect.collidepoint(pos):
            game_state.paused = False
            game_state.game_active = True
            game_state.start_ticks += pygame.time.get_ticks() - game_state.paused_ticks
    elif game_state.game_over and game_over_button_rect.collidepoint(pos):
        reset_game()
    elif game_state.stage_select:  # 스테이지 선택 처리
        if stage_1_button_rect.collidepoint(pos):
            start_game(1)
        elif stage_2_button_rect.collidepoint(pos):
            start_game(2)
        elif stage_3_button_rect.collidepoint(pos):
            start_game(3)
        elif stage_4_button_rect.collidepoint(pos):
            start_game(4)
    elif game_state.round_clear:
        if game_state.stage == 4 and start_menu_button_rect.collidepoint(pos):
            game_state.stage_select = True
        elif game_state.stage != 4:
            if next_round_button_rect.collidepoint(pos):
                start_game(game_state.stage + 1)
            elif start_menu_button_rect.collidepoint(pos):
                game_state.stage_select = True
    elif button_rect.collidepoint(pos) and not game_state.game_over:
        game_state.stage_select = True

# 게임 초기화 함수
def reset_game():
    game_state.game_active = False
    game_state.game_over = False
    game_state.round_clear = False
    game_state.paused = False
    game_state.lives = 3
    game_state.ball.x = screen_width // 2
    game_state.ball.y = game_state.paddle.y - game_state.ball.radius
    game_state.ball.speed_x = 0
    game_state.ball.speed_y = 0
    game_state.paddle.color = BLUE
    game_state.paddle.gun_active = False
    game_state.ball.piercing = False
    game_state.paddle.width = game_state.paddle.default_width
    game_state.paddle.long_active = False
    game_state.paddle.long_end_time = 0
    game_state.start_ticks = pygame.time.get_ticks()
    game_state.bricks = get_stage_1_bricks()  # 초기화 시 stage 1으로 설정
    game_state.stage = 1  # stage를 1로 초기화

# 게임 시작 함수
def start_game(stage):
    game_state.game_active = True
    game_state.game_over = False
    game_state.round_clear = False
    game_state.stage_select = False
    game_state.ball.x = screen_width // 2
    game_state.ball.y = game_state.paddle.y - game_state.ball.radius
    game_state.ball.speed_x = 0
    game_state.ball.speed_y = 0
    game_state.paddle.color = BLUE
    game_state.paddle.gun_active = False
    game_state.ball.piercing = False
    game_state.paddle.width = game_state.paddle.default_width
    game_state.paddle.long_active = False
    game_state.paddle.long_end_time = 0
    game_state.start_ticks = pygame.time.get_ticks()
    game_state.stage = stage  # 선택한 stage 설정

    if stage == 1:
        game_state.bricks = get_stage_1_bricks()
    elif stage == 2:
        game_state.bricks = get_stage_2_bricks()
    elif stage == 3:
        game_state.bricks = get_stage_3_bricks()
    elif stage == 4:
        game_state.bricks = get_stage_4_bricks()

# 게임 업데이트 함수
def update_game():
    if game_state.game_active and not game_state.game_over and not game_state.round_clear and not game_state.paused:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and game_state.paddle.x > 0:
            game_state.paddle.x -= game_state.paddle.speed
        if keys[pygame.K_RIGHT] and game_state.paddle.x < screen_width - game_state.paddle.width:
            game_state.paddle.x += game_state.paddle.speed

        if game_state.ball.speed_y == 0:
            game_state.ball.x = game_state.paddle.x + game_state.paddle.width // 2

        game_state.ball.x += game_state.ball.speed_x
        game_state.ball.y += game_state.ball.speed_y

        if game_state.ball.x - game_state.ball.radius <= 0 or game_state.ball.x + game_state.ball.radius >= screen_width:
            game_state.ball.speed_x = -game_state.ball.speed_x
        if game_state.ball.y - game_state.ball.radius <= 0:
            game_state.ball.speed_y = -game_state.ball.speed_y

        if game_state.paddle.y < game_state.ball.y + game_state.ball.radius < game_state.paddle.y + game_state.paddle.height and game_state.paddle.x < game_state.ball.x < game_state.paddle.x + game_state.paddle.width:
            game_state.ball.speed_y = -game_state.ball.speed_y
            hit_pos = game_state.ball.x - game_state.paddle.x
            game_state.ball.speed_x = (hit_pos - game_state.paddle.width / 2) / (game_state.paddle.width / 2) * 5
            if not game_state.paddle.gun_active and game_state.ball.piercing:
                game_state.ball.piercing = False
            if game_state.paddle.gun_active:
                game_state.ball.piercing = True
                game_state.paddle.gun_active = False
                game_state.paddle.color = BLUE

        for brick in game_state.bricks[:]:
            if brick.collidepoint(game_state.ball.x, game_state.ball.y):
                game_state.bricks.remove(brick)
                if not game_state.ball.piercing:
                    game_state.ball.speed_y = -game_state.ball.speed_y
                if random.random() < game_state.item_drop_chance:
                    item_x = brick.x + (brick.width - 20) // 2
                    item_y = brick.y
                    item_type = random.choice(game_state.item_types)
                    game_state.items.append({'rect': pygame.Rect(item_x, item_y, 20, 20), 'type': item_type})
                break

        if game_state.ball.y + game_state.ball.radius >= screen_height:
            game_state.lives -= 1
            if game_state.lives <= 0:
                game_state.game_active = False
                game_state.game_over = True
                game_state.final_time = (pygame.time.get_ticks() - game_state.start_ticks) // 1000  # 게임 오버 시 final_time 설정
            else:
                game_state.ball.x = game_state.paddle.x + game_state.paddle.width // 2
                game_state.ball.y = game_state.paddle.y - game_state.ball.radius
                game_state.ball.speed_x = 0
                game_state.ball.speed_y = 0
                game_state.ball.piercing = False
                game_state.paddle.color = BLUE
                game_state.paddle.width = game_state.paddle.default_width
                game_state.paddle.gun_active = False
                game_state.paddle.long_active = False
                game_state.paddle.long_end_time = 0

        if not game_state.bricks:
            game_state.game_active = False
            game_state.round_clear = True
            game_state.final_time = (pygame.time.get_ticks() - game_state.start_ticks) // 1000  # 라운드 클리어 시 final_time 설정

        for item in game_state.items[:]:
            item['rect'].y += 4
            if item['rect'].y > screen_height:
                game_state.items.remove(item)
            elif game_state.paddle.y < item['rect'].y + 20 < game_state.paddle.y + game_state.paddle.height and game_state.paddle.x < item['rect'].x < game_state.paddle.x + game_state.paddle.width:
                game_state.items.remove(item)
                if item['type'] == 'item_random':
                    item['type'] = random.choice(['item_gun', 'item_long', 'item_heart'])
                if item['type'] == 'item_gun':
                    game_state.paddle.color = PURPLE
                    game_state.paddle.gun_active = True
                elif item['type'] == 'item_long':
                    if game_state.paddle.long_active:
                        game_state.paddle.long_end_time += 7000
                    else:
                        game_state.paddle.width = int(game_state.paddle.width * 1.3)
                        game_state.paddle.long_active = True
                        game_state.paddle.long_end_time = pygame.time.get_ticks() + 7000
                ########################### PHASE 2 ##############################
                elif item['type'] == 'item_up_and_down':
                    if game_state.paddle.up_and_down_active:
                        game_state.paddle.up_and_down_end_time += 7000
                    else:
                        game_state.paddle.height = int(game_state.paddle.height * 1.3)
                        game_state.paddle.up_and_down_active = True
                        game_state.paddle.up_and_down_end_time = pygame.time.get_ticks() + 7000
                ########################### PHASE 2 ##############################
                elif item['type'] == 'item_heart':
                    game_state.lives += 1

        for item in game_state.items:
            screen.blit(item_images[item['type']], item['rect'])

        if game_state.paddle.long_active and pygame.time.get_ticks() > game_state.paddle.long_end_time:
            game_state.paddle.width = game_state.paddle.default_width
            game_state.paddle.long_active = False

# 게임 렌더링 함수
def render_game():
    screen.fill(BLACK)
    
    # seconds 변수를 함수의 맨 처음에 정의
    seconds = (pygame.time.get_ticks() - game_state.start_ticks) // 1000

    if game_state.stage_select:  # 스테이지 선택 화면 렌더링
        render_stage_select()
    elif game_state.game_active and not game_state.game_over and not game_state.round_clear and not game_state.paused:
        pygame.draw.rect(screen, game_state.paddle.color, (game_state.paddle.x, game_state.paddle.y, game_state.paddle.width, game_state.paddle.height))
        pygame.draw.circle(screen, RED, (game_state.ball.x, game_state.ball.y), game_state.ball.radius)
        for brick in game_state.bricks:
            pygame.draw.rect(screen, WHITE, brick)
        for item in game_state.items:
            screen.blit(item_images[item['type']], item['rect'])
        time_text = tiny_font.render(f"Time: {seconds}", True, WHITE)
        screen.blit(time_text, (screen_width - 100, 15))
    else:
        if game_state.game_over:
            text = font.render("Game Over", True, RED)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2 - 50))
            pygame.draw.rect(screen, BLUE, game_over_button_rect)
            screen.blit(game_over_button_text, game_over_button_text_rect)
            final_time_text = font.render(f"Time: {game_state.final_time} seconds", True, RED)  # final_time 사용
            screen.blit(final_time_text, (screen_width // 2 - final_time_text.get_width() // 2, screen_height // 2 - final_time_text.get_height() // 2 + 20))
        elif game_state.round_clear:
            if game_state.stage == 4:
                text = font.render("Ending : Final Round Clear", True, RED)
                screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2 - 50))
                final_time_text = font.render(f"Time: {game_state.final_time} seconds", True, RED)
                screen.blit(final_time_text, (screen_width // 2 - final_time_text.get_width() // 2, screen_height // 2 - final_time_text.get_height() // 2 + 20))
                pygame.draw.rect(screen, BLUE, start_menu_button_rect)
                screen.blit(start_menu_button_text, start_menu_button_text_rect)
            else:
                text = font.render("Round Clear", True, RED)
                screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2 - 50))
                final_time_text = font.render(f"Time: {game_state.final_time} seconds", True, RED)
                screen.blit(final_time_text, (screen_width // 2 - final_time_text.get_width() // 2, screen_height // 2 - final_time_text.get_height() // 2 + 20))
                pygame.draw.rect(screen, BLUE, next_round_button_rect)
                pygame.draw.rect(screen, BLUE, start_menu_button_rect)
                screen.blit(next_round_button_text, next_round_button_text_rect)
                screen.blit(start_menu_button_text, start_menu_button_text_rect)
        elif game_state.paused:
            pygame.draw.rect(screen, BLUE, reset_button_rect)
            pygame.draw.rect(screen, BLUE, resume_button_rect)
            screen.blit(reset_button_text, reset_button_text_rect)
            screen.blit(resume_button_text, resume_button_text_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)
            screen.blit(button_text, button_text_rect)

    for i in range(game_state.lives):
        x_pos = screen_width - 92 + (i % 3) * 25
        y_pos = screen_height - 30 - (i // 3) * 25
        screen.blit(heart_image, (x_pos, y_pos))

    if game_state.game_active and game_state.ball.speed_y == 0 and not game_state.game_over and not game_state.round_clear and not game_state.paused:
        press_space_text = small_font.render("Press Space", True, WHITE)
        screen.blit(press_space_text, (screen_width // 2 - press_space_text.get_width() // 2, screen_height // 2 + 50))

    pygame.display.flip()


# 스테이지 선택 화면 렌더링 함수
def render_stage_select():
    screen.fill(BLACK)
    stage_select_text = font.render("Select Stage", True, WHITE)
    screen.blit(stage_select_text, (screen_width // 2 - stage_select_text.get_width() // 2, screen_height // 4))
    
    pygame.draw.rect(screen, BLUE, stage_1_button_rect)
    pygame.draw.rect(screen, BLUE, stage_2_button_rect)
    pygame.draw.rect(screen, BLUE, stage_3_button_rect)
    pygame.draw.rect(screen, BLUE, stage_4_button_rect)
    
    screen.blit(stage_1_button_text, stage_1_button_text_rect)
    screen.blit(stage_2_button_text, stage_2_button_text_rect)
    screen.blit(stage_3_button_text, stage_3_button_text_rect)
    screen.blit(stage_4_button_text, stage_4_button_text_rect)
    
    pygame.display.flip()

# 게임 상태 초기화
game_state = GameState()

# 게임 루프
running = True
while running:
    handle_events()
    update_game()
    render_game()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
