import pygame
import chess
from utils import scale_and_load

class ChessBoard:
    def __init__(self, SIZE, COL1, COL2):
        self.board = chess.Board()
        self.SIZE = SIZE
        self.COL1 = COL1
        self.COL2 = COL2
        self.arr = []
        self.pieces_images = {
            'b' : scale_and_load('./assets/images/No shadow/512h/b_bishop_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'n' : scale_and_load('./assets/images/No shadow/512h/b_knight_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'p' : scale_and_load('./assets/images/No shadow/512h/b_pawn_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'q' : scale_and_load('./assets/images/No shadow/512h/b_queen_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'r' : scale_and_load('./assets/images/No shadow/512h/b_rook_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'k' : scale_and_load('./assets/images/No shadow/512h/b_king_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'B' : scale_and_load('./assets/images/No shadow/512h/w_bishop_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'N' : scale_and_load('./assets/images/No shadow/512h/w_knight_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'P' : scale_and_load('./assets/images/No shadow/512h/w_pawn_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'Q' : scale_and_load('./assets/images/No shadow/512h/w_queen_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'R' : scale_and_load('./assets/images/No shadow/512h/w_rook_png_512px.png', (self.SIZE // 8, self.SIZE // 8)),
            'K' : scale_and_load('./assets/images/No shadow/512h/w_king_png_512px.png', (self.SIZE // 8, self.SIZE // 8))
        }
        self.selected_square = None
        self.last_selected_square = None

    def create_board(self, screen):
        xloc = 0
        yloc = 0
        for i in  range(8):
            for j in range(8):
                col = self.COL1 if (i + j) % 2 == 0 else self.COL2
                rect = pygame.Rect(xloc, yloc, self.SIZE // 8, self.SIZE // 8)
                pygame.draw.rect(screen, col, rect)
                self.arr.append(rect)
                xloc += self.SIZE // 8
            xloc = 0
            yloc += self.SIZE // 8
        pygame.display.update()
        
    def fetch_and_assign_pieces(self, screen):
        for square, piece in self.board.piece_map().items():
            if (piece.symbol() == '.'):
                continue
            screen.blit(self.pieces_images[piece.symbol()], self.arr[square])
        pygame.display.update()
                
    def get_square_from_mouse(self, pos):
        x, y = pos
        square_x = x // (self.SIZE // 8)
        square_y = y // (self.SIZE // 8)
        return square_y * 8 + square_x 
    
    def handle_click(self, pos):
        square = self.get_square_from_mouse(pos)
        if self.last_selected_square is None:
            self.last_selected_square = square
            self.selected_square = square
        else:
            move = chess.Move(self.last_selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)    
            self.last_selected_square = None
                
    def highlight_square(self, screen, square):
        if square is not None:
            rect = self.arr[square]
            pygame.draw.rect(screen, (0, 255, 0), rect, 3)
        
    def highlight_legal_moves(self, screen, square):
        for move in self.board.legal_moves:
            if move.from_square == square:
                rect = self.arr[move.to_square]
                pygame.draw.rect(screen, (0, 255, 0), rect, 3)

