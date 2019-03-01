import pygame
from settings import enemy_image
from constants import *
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        raw_surface = pygame.image.load(enemy_image).convert_alpha()

        scale_coefficient = ENEMY_SHIP_WIDTH / raw_surface.get_rect().width
        self.image =pygame.transform.rotozoom(
            raw_surface,\
            180,\
            scale_coefficient\
        )

        self.rect = self.image.get_rect()
        Misha=self.rect.width/2
        x = randint(0 + Misha, WIDTH + Misha)  
        self.rect.midtop = (x, 20)
        
        

