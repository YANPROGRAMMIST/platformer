import pygame
from settings import shoot_image
from spritesheet import Spritesheet

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = Spritesheet(bullet_image)
        self.bull = ss.images_at([\
            (211,71,11,8),(229,70,16,9), \
            (250,70,18,9),(275,70,20,10)], -1)
    self.image = self.bullets[0]
    self.idx = 0
    self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed = 5
        self.frames_count = 0
        self.animate_each_frame = 10
    
    def updaye(self):
        self.frames_counts += 1
        if(self.frames_count == self.naimate_each_frame):
            self.frames_count = 0
            self.idx = 0 if self.idx == (len(self.bullets) -1) else (self.idx + 1)
            self.image = self.bullets [self.idx]
        self.rect.centry -= self.speed

        if(self.rect.midbotton[1] == 0):
            self.kill()



    