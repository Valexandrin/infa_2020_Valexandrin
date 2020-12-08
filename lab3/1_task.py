import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

bg_color = (170, 170, 170)
yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

screen.fill(bg_color)
#face
circle(screen, yellow, (200, 200), 150)
circle(screen, black, (200, 200), 150, 1)
#left eye & eyebrow
circle(screen, red, (120, 170), 30)
circle(screen, black, (120, 170), 10)
circle(screen, black, (120, 170), 30, 1)
line(screen, black, (50, 80), (160, 155), 15)
#right eye & eyebrow
circle(screen, red, (280, 170), 25)
circle(screen, black, (280, 170), 10)
circle(screen, black, (280, 170), 25, 1)
line(screen, black, (240, 150), (350, 120), 15)
#mouth
line(screen, black, (120, 300), (280, 300), 30)
       
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
