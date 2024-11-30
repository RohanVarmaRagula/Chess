import pygame

pygame.init()

SIZE = 600
COL1 = (139, 69, 19)
COL2 = (245, 222, 179)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60 
clock = pygame.time.Clock()
font = pygame.font.Font('./assets/fonts/static/Quicksand-Medium.ttf', 30)

def scale_and_load(path, size):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, size)
    return img