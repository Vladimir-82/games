import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen_size_x=800
screen_size_y=800
screen = pygame.display.set_mode((screen_size_x, screen_size_y))

center_x=screen_size_x//2
center_y=screen_size_y//2
smile_diametr=200

circle(screen, (255, 255, 0), (center_x, center_x), smile_diametr)
for x_ey

#rect(screen, (255, 0, 255), (100, 100, 200, 200))
#rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
#polygon(screen, (255, 255, 0), [(100,100), (200,50),(300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),(300,100), (100,100)], 5)

#circle(screen, (255, 255, 255), (200, 175), 50, 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()