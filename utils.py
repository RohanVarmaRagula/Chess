import pygame

def scale_and_load(path, size):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, size)
    return img