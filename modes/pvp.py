import chess
import pygame
from Chessboard import ChessBoard
from utils import FPS, clock
from handle_things import handle_display, handle_mousebuttondown_movement

def player_vs_player(screen, cb:ChessBoard):
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mousebuttondown_movement(screen, cb, event)
            
        if cb.check_outcome():
            running = False
            
        handle_display(screen, cb)
        pygame.display.update()
        
        