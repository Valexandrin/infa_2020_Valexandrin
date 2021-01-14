import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))
font_name = pygame.font.match_font('arial', 1)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    ''' Func draws new ball at random position with random radius and color '''
    global x, y, r, ball
    
    for i in range(3):
        x = randint(100, 1100)
        y = randint(100, 800)
        r = randint(10, 100)
        color = COLORS[randint(0, 5)]
        ball = circle(screen, color, (x, y), r)
        print(ball)

def ball_move():
    for unit in ball:
        
        unit.move(2, 0)
        print(ball)

def hit_counter(event):
    ''' Func handles mouse click and counts quantity of success hits to ball '''
    global score
    dist = ((x - event[0])**2 + (y - event[1])**2) ** (1/2)
    print(x, y, r, dist)    
    if r >= dist:
        score += 1

def draw_text(surf, text, size):
    ''' Func draws text at top of game display '''
    font = pygame.font.Font(font_name, size)
    text = font.render(text, True, WHITE)
    textpos = text.get_rect()
    textpos.centerx = surf.get_rect().centerx
    surf.blit(text, textpos)
    
pygame.display.update()
clock = pygame.time.Clock()
score = 0
new_ball()

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:            
            hit_counter(event.pos)          
            print(score)

    draw_text(screen, 'Hits - '+str(score), 25)
    ball = ball.move(2, 0)
   
    print(ball)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
