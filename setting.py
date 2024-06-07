import pygame

# ȭ�� ����
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Game")

# ����
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

# ��Ʈ ����
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
tiny_font = pygame.font.Font(None, 24)

# ��Ʈ �̹��� �ε�
heart_image = pygame.image.load('images/heart.png')
heart_image = pygame.transform.scale(heart_image, (20, 20))

# ������ �̹��� �ε�
item_images = {
    'item_gun': pygame.transform.scale(pygame.image.load('images/item_gun.png'), (20, 20)),
    'item_long': pygame.transform.scale(pygame.image.load('images/item_long.png'), (20, 20)),
    'item_heart': pygame.transform.scale(pygame.image.load('images/heart.png'), (20, 20)),
    'item_random': pygame.transform.scale(pygame.image.load('images/item_random.png'), (20, 20)),
    ########################### PHASE 2 ##############################
    'item_up_and_down': pygame.transform.scale(pygame.image.load('images/item_up_and_down.png'),(20,20))
    ########################### PHASE 2 ##############################
}
