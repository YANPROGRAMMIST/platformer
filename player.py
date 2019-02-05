import pygame
import os
from settings import player_image
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(player_image).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDHT/2,HEIGHT/2)