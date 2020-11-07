from math import sqrt
import pygame
from pygame.draw import *
def draw(hight, weght):
    """Рисует окружность, описывающую прямоугольник"""
    pygame.init()
    FPS = 1
    display_x=1000
    display_y=1000

    screen = pygame.display.set_mode((display_x, display_y))

    begin_point_x=int(display_x/2)-int(weght/2)
    begin_point_y=int(display_y/2)-int(hight/2)

    diametr=int(sqrt(pow(weght, 2) + pow(hight, 2)))
    print(f'Диаметр окружности={diametr}', end=' мм')
    rect(screen, (0, 0, 255), (begin_point_x, begin_point_y, weght, hight), 1)
    circle(screen, (255, 255, 255), (int(display_x/2), int(display_y/2)), int(diametr/2), 1)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True


    pygame.quit()

hight=608
weght=750
draw(hight, weght)