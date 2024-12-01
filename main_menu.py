import pygame
from utils import SIZE, WHITE, BLACK

def main_menu(screen, font):
    menu_options = ['Player vs Player', 'CPU Easy', 'CPU Medium', 'CPU Hard']
    screen.fill(BLACK)
    option_rects = []
        
    for i, option in enumerate(menu_options):
        text_surface = font.render(option, True, BLACK)
        rect = text_surface.get_rect()
        rect.topleft = (SIZE // 3, SIZE // 4 + i * SIZE // 8)
        pygame.draw.rect(screen, WHITE, rect)
        screen.blit(text_surface, (SIZE // 3, SIZE // 4 + i * SIZE // 8))
        option_rects.append(rect)
        
    pygame.display.update()

    selected_option = -1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                cursor_changed = False
                
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(pos):
                        if not cursor_changed:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                            cursor_changed = True
                            break
                
                if not cursor_changed:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        selected_option = i
                        running = False
                        
    return selected_option                
 