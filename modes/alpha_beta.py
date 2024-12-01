import chess
import pygame
import math
from Chessboard import ChessBoard
from utils import clock, FPS
from handle_things import handle_display, handle_mousebuttondown_movement

def eval(cb:ChessBoard):
    return cb.score(chess.BLACK) - cb.score(chess.WHITE)

def choose_best_move_by_alphabeta(cb : ChessBoard, max_depth, alpha = -math.inf, beta = math.inf, maximizer = True):
    if max_depth == 0:
        return None, eval(cb)
    
    best_move = None
    best_score = -math.inf if maximizer else math.inf
    
    if maximizer:
        for move in cb.board.legal_moves:
            cb.board.push(move)
            _, next_score = choose_best_move_by_alphabeta(cb, max_depth - 1, alpha, beta, not maximizer)
            cb.board.pop()
            if next_score > best_score:
                best_score = next_score
                best_move = move
            alpha = max(alpha, next_score)
            if alpha >= beta:
                break        
    else:
        for move in cb.board.legal_moves:
            cb.board.push(move)
            _, next_score = choose_best_move_by_alphabeta(cb, max_depth - 1, alpha, beta, not maximizer)
            cb.board.pop()
            if next_score < best_score:
                best_score = next_score
                best_move = move
            beta = min(beta, next_score)
            if alpha >= beta:
                break
        
    return best_move, best_score
    
        
def alpha_beta(screen, cb:ChessBoard, difficulty): # Always black is the agent
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
            best_move, _ = choose_best_move_by_alphabeta(cb, difficulty)
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
             