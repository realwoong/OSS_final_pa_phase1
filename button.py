import pygame
from setting import screen_width, screen_height, small_font, font, WHITE, BLUE

# 버튼 설정
reset_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 50, 300, 50)
resume_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 10, 300, 50)
reset_button_text = small_font.render("Restart Game", True, WHITE)
resume_button_text = small_font.render("Resume Game", True, WHITE)
reset_button_text_rect = reset_button_text.get_rect(center=reset_button_rect.center)
resume_button_text_rect = resume_button_text.get_rect(center=resume_button_rect.center)

# Next Round 및 Start Menu 버튼 설정
next_round_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 50, 300, 50)
start_menu_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 120, 300, 50)
next_round_button_text = small_font.render("Next Round", True, WHITE)
start_menu_button_text = small_font.render("Start Menu", True, WHITE)
next_round_button_text_rect = next_round_button_text.get_rect(center=next_round_button_rect.center)
start_menu_button_text_rect = start_menu_button_text.get_rect(center=start_menu_button_rect.center)

game_over_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 50, 300, 50)
game_over_button_text = small_font.render("Restart Game", True, WHITE)
game_over_button_text_rect = game_over_button_text.get_rect(center=game_over_button_rect.center)

button_color = BLUE
button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 50, 300, 100)
button_text = font.render("Game Start", True, WHITE)
button_text_rect = button_text.get_rect(center=button_rect.center)

# 스테이지 선택 버튼 설정
stage_1_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 60, 200, 50)
stage_2_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50)
stage_3_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 60, 200, 50)
stage_4_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 120, 200, 50)

stage_1_button_text = small_font.render("Stage 1", True, WHITE)
stage_2_button_text = small_font.render("Stage 2", True, WHITE)
stage_3_button_text = small_font.render("Stage 3", True, WHITE)
stage_4_button_text = small_font.render("Stage 4", True, WHITE)

stage_1_button_text_rect = stage_1_button_text.get_rect(center=stage_1_button_rect.center)
stage_2_button_text_rect = stage_2_button_text.get_rect(center=stage_2_button_rect.center)
stage_3_button_text_rect = stage_3_button_text.get_rect(center=stage_3_button_rect.center)
stage_4_button_text_rect = stage_4_button_text.get_rect(center=stage_4_button_rect.center)
