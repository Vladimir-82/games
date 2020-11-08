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
eye_diametr=smile_diametr//4

circle(screen, (255, 255, 0), (center_x, center_y), smile_diametr)

for x_eye, y_eye in (center_x-2*eye_diametr, center_y-eye_diametr), (center_x+2*eye_diametr, center_y-eye_diametr):
    circle(screen, (255, 0, 0), (x_eye, y_eye), eye_diametr)
    circle(screen, (0, 0, 0), (x_eye, y_eye), eye_diametr//2)

rect(screen, (0, 0, 0), (center_x-2*eye_diametr, center_y+eye_diametr, 4*eye_diametr, eye_diametr))


line(screen, (0, 0, 255), (center_x-eye_diametr//2, center_y-eye_diametr), (center_x-2*eye_diametr, center_y-3*eye_diametr), 20)
line(screen, (0, 0, 255), (center_x+eye_diametr//2, center_y-eye_diametr), (center_x+3*eye_diametr, center_y-4*eye_diametr), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()