import pygame
from Chessboard import ChessBoard
from main_menu import main_menu
from utils import SIZE, COL1, COL2, font
from modes.pvp import player_vs_player   
                
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Chess')
    screen = pygame.display.set_mode((SIZE, SIZE + 50))
    option = main_menu(screen, font)

    cb = ChessBoard(SIZE, COL1, COL2)
    cb.create_board(screen)
    cb.fetch_and_assign_pieces(screen)

    if option == 0: # Player vs Player
        player_vs_player(screen, cb)
    elif option == 1: # CPU Easy
        pass
    elif option == 2: # CPU Medium
        pass
    elif option == 3: # CPU Hard
        pass
    else:
        pygame.quit()

    pygame.quit()
