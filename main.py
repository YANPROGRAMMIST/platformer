import pygame
from constants import *
from player import Player
from enemy import Enemy
from level1 import Level1
from shoot import Shoot

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption(World)
clock = pygame.time.Clock()

running = True

all_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy()
all_sprites.add(player)
all_sprites.add(enemy)

level1 = Level1()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                (x, y) = player.rect.midtop
                all_sprites.add(Shoot(x, y))
    
    level1.update()
    all_sprites.update()

    colided = all_sprites.

    screen.fill(RED)
    level1.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
    


     