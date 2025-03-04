import chess
import random
import pygame
from Chessboard import ChessBoard
from utils import clock, FPS
from handle_things import handle_display, handle_mousebuttondown_movement

def eval(cb:ChessBoard):
    return cb.score(chess.BLACK) - cb.score(chess.WHITE)

def choose_best_move_by_minimax(cb:ChessBoard, max_depth = 3, maximizer = True):
    if max_depth == 0:
        return None, eval(cb)
    
    best_move = None
    best_score = float('-inf') if maximizer else float('inf')
    
    for move in cb.board.legal_moves:
        cb.board.push(move)
        _, next_score = choose_best_move_by_minimax(cb, max_depth - 1, not maximizer)
        cb.board.pop()
        
        if (maximizer and next_score >= best_score) or (not maximizer and next_score <= best_score):
            if next_score == best_score:
                best_move = random.choice([move, best_move])
            else:
                best_move = move
            best_score = next_score
            
    return best_move, best_score
        
def mini_max(screen, cb:ChessBoard, difficulty): # Always black is the agent
    running = True
    while running:
        clock.tick(FPS)
        if cb.turn() == chess.WHITE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                handle_mousebuttondown_movement(screen, cb, event)
        
        handle_display(screen, cb)
        pygame.display.update()
        
        if cb.check_outcome():
            running = False
            break
        
        if cb.turn() == chess.BLACK:
            best_move, _ = choose_best_move_by_minimax(cb, difficulty)
            if best_move is not None:
                cb.board.push(best_move)
            cb.create_board(screen)  
            cb.fetch_and_assign_pieces(screen)  
            cb.highlight_square(screen, best_move.from_square)
            cb.highlight_square(screen, best_move.to_square)
        handle_display(screen, cb)
        pygame.display.update()
        
        if cb.check_outcome():
            running = False
             