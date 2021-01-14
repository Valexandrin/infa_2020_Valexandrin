import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 20

screen = pygame.display.set_mode((1200, 900))
right = screen.get_rect().right
left = screen.get_rect().left
top = screen.get_rect().top
bottom = screen.get_rect().bottom

font_name = pygame.font.match_font('arial', 1)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [WHITE, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def balls_creation():
    ''' Function sets for each ball random coordinates of center, radius,
        velocity (step length for both axes) and ball's color. The parameters
        for each ball put into a list '''
    global A
    A = []
    for i in range(5):
        x = randint(left + 100, right - 100)
        y = randint(top + 100, bottom - 100)
        r = randint(10, 100)
        step_x = randint(-30, 30)
        step_y = randint(-30, 30)
        color = COLORS[randint(0, 5)]
        A = A + [(x, y, r, step_x, step_y, color)]
     
def new_ball():
    ''' Function draws balls by the list of parameters '''    
    for x, y, r, step_x, step_y, color in A:         
        circle(screen, color, (x, y), r)

def coords_update():
    ''' Function updates the list of parameters for each ball '''
    global A
    B = []    
    for x, y, r, step_x, step_y, color in A:  
        x, y, step_x, step_y, color = check_frame_hit(x, y, r,
                                                      step_x, step_y, color)
        B = B + [(x, y, r, step_x, step_y, color)]   
    A = []   
    A = A + B

def check_frame_hit(x, y, r, step_x, step_y, color):
    ''' Function checks if a ball hit screen frame and return updated
        parameters: coordinates and velocityб color '''
    if x - r + step_x <= left or x + r + step_x >= right:
        step_x = update_step(step_x)
        step_y = randint(-30, 30)
        x += step_x
        y += step_y
        color = COLORS[randint(0, 5)]
    elif y - r + step_y <= top or y + r + step_y >= bottom:
        step_x = randint(-30, 30)
        step_y = update_step(step_y)
        x += step_x
        y += step_y
        color = COLORS[randint(0, 5)]
    else:
        x += step_x
        y += step_y
    return x, y, step_x, step_y, color

def update_step(step):
    ''' Function updates ball's velocity '''
    if step < 0:
        step = randint(1, 30)
    else:
        step = randint(-30, 1)
    return step

def hit_counter(score, event):
    ''' Func handles mouse click and counts quantity of success hits to ball '''
    for x, y, r, step_x, step_y, color in A:
        dist = ((x - event[0])**2 + (y - event[1])**2) ** (1/2)
        if r >= dist:
            score += 1
    return score

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
balls_creation()
finished = False
pygame.mouse.set_visible(False)
cursor_img = pygame.image.load('cursor_img.png')
cursor_img_rect = cursor_img.get_rect()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:            
            score = hit_counter(score, event.pos)          
            print(score)
    
    draw_text(screen, 'Hits - '+str(score), 25)
    new_ball()
    coords_update()
    cursor_img_rect.center = pygame.mouse.get_pos()
    screen.blit(cursor_img, cursor_img_rect)    
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
