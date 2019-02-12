import pygame
import os
from settings import player_image
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        raw_surface = pygame.image.load(player_image).convert_alpha()
        scale_coefficient = PLAYER_SHIP_WIDTH / raw_surface.get_rect().width
        self.image =pygame.transform.rotozoom(
            pygame.image.load(player_image).convert_alpha(),\
            180,\
            scale_coefficient\
        )

        
    self.rect = self.image.get_rect()
    self.rect.midbotton = (WIDHT / 2, HEIGHT / -20)
        self.rect.center = (WIDHT / 2,(HEIGHT / -20))