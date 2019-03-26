import pygame
from constants import *
from settings import shoot_image
from spritesheet import Spritesheet

class Shoot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ss = Spritesheet(shoot_image)
        self.bullet_images = ss.images_at([\
            (211,71,11,8),(229,70,16,9), \
            (250,70,18,9),(275,70,20,10)], -1)
        self.bullets = []
        for bullet in self.bullet_images:
            self.bullets.append(pygame.transform.rotate(bullet, 90))
        self.image = self.bullets[0]
        self.idx = 0
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.frames_count = 0
        self.animate_each_frame = 10
    
    def update(self):
        self.frames_count += 1
        if(self.frames_count == self.animate_each_frame):
            self.frames_count = 0
            self.idx = 0 if self.idx == (len(self.bullets) -1) else (self.idx + 1)
            self.image = self.bullets [self.idx]
        self.rect.centery -= self.speed

        if(self.rect.midbottom[1] == 0):
            self.kill()



    