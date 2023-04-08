import pygame
import os

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Game Cờ Vua")

# Xác định màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Lấy đường dẫn đến thư mục hiện tại
current_path = os.path.dirname(__file__)

# Tạo đường dẫn đến ảnh quân cờ
wpawn_path = os.path.join(current_path, "white_pawn.png")

# Load ảnh quân cờ
wpawn = pygame.image.load(wpawn_path)

# Vẽ bàn cờ
def draw_board(screen):
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, (row*75, col*75, 75, 75))

# Vẽ quân cờ
def draw_piece(screen, piece, x, y):
    screen.blit(piece, (x, y))

# Vẽ tất cả các quân cờ
def draw_pieces(screen):
    for row in range(8):
        for col in range(8):
            if row == 1:
                draw_piece(screen, wpawn, row*75, col*75)

# Vẽ bàn cờ và quân cờ
def draw_game(screen):
    draw_board(screen)
    draw_pieces(screen)

# Vòng lặp chính của trò chơi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Vẽ trò chơi
    draw_game(screen)

    # Cập nhật màn hình
    pygame.display.update()

# Dọn dẹp các tài nguyên của Pygame
pygame.quit()
