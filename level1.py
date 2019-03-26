import pygame
from settings import level1_image
from spritesheet import Spritesheet
from constants import *
import math

class Level1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        raw_surface = pygame.image.load(level1_image).convert()
        w = raw_surface.get_rect().width
        scale_coefficient = WIDTH / w
        
        self.images = [\
            pygame.transform.rotozoom(raw_surface, 0, scale_coefficient),\
            pygame.transform.flip(pygame.transform.rotozoom(raw_surface, 0, scale_coefficient), False, True)\
        ]

        h = self.images[0].get_rect().height 
        self.block = pygame.Surface((WIDTH, 2*h))

        self.block.blit(self.images[0], (0,0))
        self.block.blit(self.images[1], (0,h))

        self.block_height = self.block.get_rect().height

        self.speed = 5
        self.position1 = HEIGHT - self.block_height
        self.position2 = HEIGHT - 2 * self.block_height

    def update(self):
        self.position1 += self.speed
        self.position2 += self.speed
        if (self.position1 >= HEIGHT):
            self.position1 = self.position2 - self.block_height
        if (self.position2 >= HEIGHT):
            self.position2 = self.position1 - self.block_height

    def draw(self, screen):
        screen.blit(self.block, (0, self.position1))
        screen.blit(self.block, (0, self.position2))