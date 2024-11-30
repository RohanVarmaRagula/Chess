import pygame
import chess
from Chessboard import ChessBoard

pygame.init()
SIZE = 600
COL1 = (139, 69, 19)
COL2 = (245, 222, 179)
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SIZE, SIZE + 50))
pygame.display.set_caption('Chess')

font = pygame.font.Font('./assets/fonts/static/Quicksand-Medium.ttf', 30)

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
        
    if cb.check_outcome():
        running = False
        
    score_area_rect = pygame.Rect(0, SIZE, SIZE, 50)
    screen.fill((0, 0, 0), score_area_rect)
    text_surface1 = font.render(f'White score = {cb.score(chess.WHITE)}', True, (0, 200, 255)) 
    text_surface2 = font.render(f'Black score = {cb.score(chess.BLACK)}', True, (0, 200, 255)) 
    screen.blit(text_surface1, (10, SIZE + 10))
    screen.blit(text_surface2, (SIZE - 230, SIZE + 10))
    
    pygame.display.set_caption(f'Chess ({cb.turn()} to move)')
    pygame.display.update()

pygame.quit()
