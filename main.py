import pygame
from Chessboard import ChessBoard

pygame.init()
SIZE = 600
COL1 = (139, 69, 19)
COL2 = (245, 222, 179)
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Chess')

cb = ChessBoard(SIZE, COL1, COL2)
cb.create_board(screen)
cb.fetch_and_assign_pieces(screen)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cb.handle_click(event.pos)
            cb.create_board(screen)  
            cb.fetch_and_assign_pieces(screen)  
            if cb.last_selected_square is not None:
                cb.highlight_square(screen, cb.last_selected_square)
                cb.highlight_legal_moves(screen, cb.last_selected_square)  
        cb.selected_square = None
    pygame.display.update()

pygame.quit()
