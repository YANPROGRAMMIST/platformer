import pygame
from settings import level1_image
from spritesheet import Spritesheet
from constants import *

class level1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        raw_surface = pygame.image.load(level1_image).convert()
        w = raw_surface.get.rect().width
        scale_coefficient = WIDTH / w
        
        self.images = [\
            pygame.transform.rotozoom(raw_surface, 0, scale_coefficient),\
            pygame.transform.rotozoom(raw_surface, 180, scale_coefficient)\
        ]

        h = self.images[0].get_rect().height 
        self.block = pygame.Surface((WIDTH, 2*h))

        self.block.blit(self.images[0], (0,0))
        self.block.blit(self.images[1], (0,h))