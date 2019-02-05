import pygame
from constants import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDHT, HEIGHT)) 
pygame.display.set_caption(World)
clock = pygame.time.Clock()

running = True

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    all_sprites.update()
    

    screen.fill(RED)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
    


     