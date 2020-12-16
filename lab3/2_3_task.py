import numpy as nu
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1600, 1000))

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


def draw_boy(surface, x, y, width, height, col_1, col_2, col_3, col_4):
    '''
    The function draws boy.
    surface - pygame.Surface object
    x, y - image center coordinates
    width, height - image width and height
    col_1 - shirt color
    col_2 - skin_color
    col_3 - eye_color
    col_4 - hair_color
    '''
    body_y = y + height * 0.4
    body_width = width // 3
    draw_body(surface, x, body_y, body_width, col_1)

    hand_width = width // 7
    hand_height = height * 0.7
    hand_y = body_y * 0.85
    for hand_x, hand_width in ((x - hand_width * 2, - hand_width),
                               (x + hand_width * 2, hand_width)):
        draw_hand(surface, hand_x, hand_y, hand_width, hand_height, body_width,
                  col_1, col_2)

    face_width = body_width * 0.85
    face_heigth = face_width
    draw_face(surface, x, y, face_width, face_heigth, col_2, col_3)

    draw_hair(surface, x, y, face_width, face_heigth * 1.2, col_4)


def draw_body(surface, x, y, width, col_1): 
    '''
    The function draws boy's body.
    surface - pygame.Surface object
    x, y - image center coordinates
    width - image width
    col_1 - shirt color
    '''
    circle(surface, col_1, (x, y), width)

    
def draw_hand(surface, x, y, width, height, thickness, col_1, col_2):
    '''
    The function draws boy's hand.
    surface - pygame.Surface object
    x, y - shoulder coordinates
    width, height - image width and height
    thickness - hand thickness
    col_1 - shirt color
    col_2 - skin_color
    '''
    line(surface, col_2, (x, y), (x + width, y - height), thickness // 7)
    circle(surface, col_2, (x + width, y - height), thickness // 6)
    S = [(x + width // 2, y - height // 14),
         (x + width // 2, y + height // 11),
         (x - width // 3, y + height // 9),
         (x - width, y - height // 20),
         (x - width // 3, y - height // 8)]
    polygon(surface, col_1, S)
    polygon(surface, black, S, 1)
    

def draw_face(surface, x, y, width, height, col_2, col_3):
    '''
    The function draws boy's face.
    surface - pygame.Surface object
    x, y - image center coordinates
    width, height - image width and height
    col_2 - skin_color
    col_3 - eye_color
    col_4 - hair_color
    '''    
    circle(surface, col_2, (x, y), width)
    eye_y = y - height // 5
    eye_width = width // 3
    eye_height = height // 3.5
    for eye_x in (x - width // 3, x + width // 3):
        draw_eye(surface, eye_x, eye_y, eye_width, eye_height, col_3)
    
    draw_nose(surface, x, y + height // 10, width // 6, height // 6)

    draw_mouth(surface, x, y + height // 2.5, width, height // 3)


def draw_eye(surface, x, y, width, height, col_3):
    '''
    The function draws boy's eye.
    surface - pygame.Surface object
    x, y - image center coordinates
    width, height - image width and height
    col_3 - eye_color
    '''
    ellipse(surface, col_3, (x - width // 2, y - height // 2, width, height))
    ellipse(surface, black, (x - width // 2, y - height // 2, width, height), 1)
    ellipse(surface, black, (x - width // 6, y - height // 8,
                             width // 3, height // 3))
   

def draw_nose(surface, x, y, width, height):
    '''
    The function draws boy's nose.
    surface - pygame.Surface object
    x, y - image center coordinates
    width, height - image width and height
    '''
    N = [(x - width // 2, y - height // 2),
         (x + width // 2, y - height // 2),
         (x, y + height // 2)]
    polygon(screen, сhoco, N)
    polygon(screen, black, N, 1)


def draw_mouth(surface, x, y, width, height):
    '''
    The function draws boy's mouth.
    surface - pygame.Surface object
    x, y - image center coordinates
    width, height - image width and height
    '''
    M = [(x - width // 2, y - height // 2),
         (x + width // 2, y - height // 2),
         (x, y + height // 2)]
    polygon(surface, red, M)
    polygon(surface, black, M, 1)


def draw_hair(surface, x, y, width, height, col_4):
    '''
    The function draws boy's hair.
    surface - pygame.Surface object
    x, y - image center coordinates
    width, height - image width and height
    col_4 - hair_color
    '''
    for a in range (45, 135, 10):
            a_1 = nu.deg2rad(a)
            a_2 = nu.deg2rad(a+12)
            a_3 = nu.deg2rad(a+6)
            HAIR = [(x + width * nu.cos(a_1), y - width * nu.sin(a_1)),
                    (x + width * nu.cos(a_2), y - width * nu.sin(a_2)),
                    (x + height * nu.cos(a_3), y - height * nu.sin(a_3))]
            polygon(surface, col_4, HAIR)
            polygon(surface, black, HAIR, 1)
   
def draw_table(surface, x, height):
    '''
    The function draws table at the top of picture.
    surface - pygame.Surface object
    x - image center coordinate
    height - font's height
    '''
    fontObj = pygame.font.Font(None, height)
    textSurfaceObj = fontObj.render('PYTHON is REALLY AMAZING',
                                    True, black, green)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, height // 3)
    surface.blit(textSurfaceObj, textRectObj)


#left boy drawing
draw_boy(screen, 450, 550, 800, 1000, green, lt_yellow, PaleGoldenrod, yellow)
#right boy drawing
draw_boy(screen, 1150, 550, 800, 1000, orange, lt_yellow, blue, purple)
#draw_table
draw_table(screen, 800, 155)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
