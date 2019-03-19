import pygame
from settings import level1_image
from spritesheet import Spritesheet

class level1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        raw_surface = pygame.image.load(level1_image).convert()
        w = raw_surface.get.rect().width
        scale_coefficient = WIDTH / w
