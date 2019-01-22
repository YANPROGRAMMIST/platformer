import pygame

WIDHT = 640
HEIGHT = 480
FPS = 60
World = 'Platformer'


RED = (255,0,0)
pygame.init()
screen = pygame.display.set_mode((WIDHT, HEIGHT)) 
pygame.display.set_caption(World)
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    

    screen.fill(RED)
    pygame.display.flip()

pygame.quit()
    