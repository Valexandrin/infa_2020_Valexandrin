import numpy as nu
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
SIZE = 1000

screen = pygame.display.set_mode((SIZE, SIZE))

blue = (135, 206, 235)
yellow = (255, 255, 0)
lt_yellow = (255, 255, 224)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255,0)
сhoco = (210, 105, 30)
orange = (255, 165, 0)

#body with hands
circle(screen, orange, (SIZE/2, SIZE), 320)
line(screen, lt_yellow, (SIZE/2 - 250, SIZE - 250), (100, 100), 50)
circle(screen, lt_yellow, (100, 100), 50)
line(screen, lt_yellow, (SIZE/2 + 250, SIZE - 250), (900, 100), 50)
circle(screen, lt_yellow, (900, 100), 50)
LH = [(SIZE/2 - 220, SIZE - 170),
       (SIZE/2 - 170, SIZE - 270),
       (SIZE/2 - 220, SIZE - 350),
       (SIZE/2 - 320, SIZE - 320),
       (SIZE/2 - 300, SIZE - 220)]
polygon(screen, orange, LH)
polygon(screen, black, LH, 1)
RH = [(SIZE/2 + 220, SIZE - 170),
      (SIZE/2 + 170, SIZE - 270),
      (SIZE/2 + 220, SIZE - 350),
      (SIZE/2 + 320, SIZE - 320),
      (SIZE/2 + 300, SIZE - 220)]
polygon(screen, orange, RH)
polygon(screen, black, RH, 1)
#face
circle(screen, lt_yellow, (SIZE/2, SIZE/2), 250)
#left eye
circle(screen, blue, (SIZE/2 - 80, SIZE/2 - 80), 50)
circle(screen, black, (SIZE/2 - 80, SIZE/2 - 80), 50, 1)
circle(screen, black, (SIZE/2 - 80, SIZE/2 - 70), 15)
#right eye
circle(screen, blue, (SIZE/2 + 80, SIZE/2 - 80), 50)
circle(screen, black, (SIZE/2 + 80, SIZE/2 - 80), 50, 1)
circle(screen, black, (SIZE/2 + 80, SIZE/2 - 70), 15)
#nose & mouth
N = [(SIZE/2 - 20, SIZE/2),
     (SIZE/2 + 20, SIZE/2),
     (SIZE/2, SIZE/2 + 40)]
polygon(screen, сhoco, N)
polygon(screen, black, N, 1)
M = [(SIZE/2 - 130, SIZE/2 + 50),
     (SIZE/2 + 130, SIZE/2 + 50),
     (SIZE/2, SIZE/2 + 130)]
polygon(screen, red, M)
polygon(screen, black, M, 1)
#table
fontObj = pygame.font.Font(None, 130)
textSurfaceObj = fontObj.render('PYTHON is AMAZING', True, black, green)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (500, 50)
screen.blit(textSurfaceObj, textRectObj)
#hair
r = 250
r_1 = 300
for a in range (45, 135, 10):
    a_1 = nu.deg2rad(a)
    a_2 = nu.deg2rad(a+12)
    a_3 = nu.deg2rad(a+6)
    HAIR = [(SIZE/2 + r * nu.cos(a_1), SIZE/2 - r * nu.sin(a_1)),
            (SIZE/2 + r * nu.cos(a_2), SIZE/2 - r * nu.sin(a_2)),
            (SIZE/2 + r_1 * nu.cos(a_3), SIZE/2 - r_1 * nu.sin(a_3))]
    print (HAIR)
    polygon(screen, yellow, HAIR)
    polygon(screen, black, HAIR, 1)
      
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
