import numpy as nu
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
SIZE_X = 1600
SIZE_Y = 1000
r = 220
r_1 = r +50
R = 300

screen = pygame.display.set_mode((SIZE_X, SIZE_Y))

blue = (135, 206, 235)
yellow = (255, 255, 0)
lt_yellow = (255, 255, 224)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255,0)
сhoco = (210, 105, 30)
orange = (255, 165, 0)
PaleGoldenrod = (238, 232, 170)
purple = (128, 0, 128)

def boy_drawing(center_x, center_y,
                shirt_color, skin_color, eye_color, hair_color):

    #body and hands
    circle(screen, shirt_color, (center_x, SIZE_Y), R)
    line(screen, skin_color, (center_x - 250, SIZE_Y - 250),
         (center_x - R, center_y * (1-0.8)), 50)
    circle(screen, skin_color, (center_x - R, center_y * (1-0.8)), 50)
    line(screen, skin_color, (center_x + 250, SIZE_Y - 250),
         (center_x + R, center_y * (1-0.8)), 50)
    circle(screen, skin_color, (center_x + R, center_y * (1-0.8)), 50)
    LH = [(center_x - 220, SIZE_Y - 170),
          (center_x - 170, SIZE_Y - 270),
          (center_x - 220, SIZE_Y - 350),
          (center_x - 320, SIZE_Y - 320),
          (center_x - 300, SIZE_Y - 220)]
    polygon(screen, shirt_color, LH)
    polygon(screen, black, LH, 1)
    RH = [(center_x + 220, SIZE_Y - 170),
          (center_x + 170, SIZE_Y - 270),
          (center_x + 220, SIZE_Y - 350),
          (center_x + 320, SIZE_Y - 320),
          (center_x + 300, SIZE_Y - 220)]
    polygon(screen, shirt_color, RH)
    polygon(screen, black, RH, 1)

    #face
    circle(screen, skin_color, (center_x, center_y), r)

    #eyes
    offset = 80
    for i in range(2):
        circle(screen, eye_color, (center_x + offset, center_y - 80), 50)
        circle(screen, black, (center_x + offset, center_y - 80), 50, 1)
        circle(screen, black, (center_x + offset, center_y - 70), 15)
        offset = - offset
    
    #nose & mouth
    N = [(center_x - 20, center_y),
         (center_x + 20, center_y),
         (center_x, center_y + 40)]
    polygon(screen, сhoco, N)
    polygon(screen, black, N, 1)
    M = [(center_x - 130, center_y + 50),
         (center_x + 130, center_y + 50),
         (center_x, center_y + 130)]
    polygon(screen, red, M)
    polygon(screen, black, M, 1)

    #hair
    for a in range (45, 135, 10):
        a_1 = nu.deg2rad(a)
        a_2 = nu.deg2rad(a+12)
        a_3 = nu.deg2rad(a+6)
        HAIR = [(center_x + r * nu.cos(a_1), center_y - r * nu.sin(a_1)),
                (center_x + r * nu.cos(a_2), center_y - r * nu.sin(a_2)),
                (center_x + r_1 * nu.cos(a_3), center_y - r_1 * nu.sin(a_3))]
        polygon(screen, hair_color, HAIR)
        polygon(screen, black, HAIR, 1)
    
#left boy drawing
boy_drawing(SIZE_X/4, SIZE_Y/2,
            green, lt_yellow, PaleGoldenrod, yellow)
#right boy drawing
boy_drawing(SIZE_X * 3/4, SIZE_Y/2,
            orange, lt_yellow, blue, purple)

#table
fontObj = pygame.font.Font(None, 150)
textSurfaceObj = fontObj.render('PYTHON is REALLY AMAZING', True, black, green)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (SIZE_X/2, 50)
screen.blit(textSurfaceObj, textRectObj)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
