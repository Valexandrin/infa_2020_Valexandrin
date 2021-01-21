import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 18

screen = pygame.display.set_mode((1200, 900))
right = screen.get_rect().right
left = screen.get_rect().left
top = screen.get_rect().top
bottom = screen.get_rect().bottom
center_x = screen.get_rect().centerx

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
        A = A + [update_param()]

def update_param():
    x = randint(left + 100, right - 100)
    y = randint(top + 100, bottom - 100)
    r = randint(25, 50)  
    step_x = update_step(0)
    step_y = update_step(0)
    color = COLORS[randint(0, 5)]
    new_param = x, y, r, step_x, step_y, color
    return new_param

def update_step(step):
    ''' Function updates ball's velocity '''
    if step == 0:
        step = randint(-30, 30)

    if step < 0:
        step = randint(5, 30)
    else:
        step = randint(-30, -5)
    return step
     
def new_ball():
    ''' Function draws balls by the list of parameters '''    
    for x, y, r, step_x, step_y, color in A:         
        circle(screen, color, (x, y), r)

def coords_update():
    ''' Function checks for each ball if it hits screen frame and return
        updated list of parameters like coordinates, velocity and color '''          
    for set_param in A:
        x, y, r, step_x, step_y, color = set_param
        if x - r + step_x <= left or x + r + step_x >= right:
            step_x = update_step(step_x)        
            step_y = update_step(0)
        elif y - r + step_y <= top or y + r + step_y >= bottom:        
            step_x = update_step(0)
            step_y = update_step(step_y)               
        x += step_x
        y += step_y
        A[A.index(set_param)] = [x, y, r, step_x, step_y, color]

def hit_counter(score, event):
    ''' Func handles mouse click and counts quantity of success hits to ball '''
    for set_param in A:
        x, y, r, step_x, step_y, color = set_param        
        dist = ((x - event[0])**2 + (y - event[1])**2) ** (1/2)
        if r >= dist:
            score += 1
            circle(screen, color, (x, y), r + 20, 5) #mark place of success hit
            A[A.index(set_param)] = update_param()
            
    return score

def draw_text(surf, text, pos_on_sceen, size):
    ''' Func draws text at top of game display '''
    font = pygame.font.Font(font_name, size)
    text_on_surf = font.render(text, True, WHITE)
    textpos = text_on_surf.get_rect()
    textpos.centerx = pos_on_sceen
    surf.blit(text_on_surf, textpos)

def check_resaults(score):
    '''
    inp = open('winners.txt', 'r')
    out = open('winners.txt', 'a')
    CURRENT_RESAULTS = inp.readlines()
    
    print(score, file=out)
    
    print(CURRENT_RESAULTS)
    inp.close()'''
    CURRENT_RESAULTS = score
    return CURRENT_RESAULTS
    
if __name__ == '__main__':
    pygame.display.update()
    clock = pygame.time.Clock()
    balls_creation()
    score = 0
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

        seconds = 15 - (pygame.time.get_ticks())//1000
        if seconds > 0:           
            draw_text(screen,
                      'Hits - '+str(score)+'  ('+str(seconds)+')',
                      center_x, 25)
            new_ball()
            coords_update()
            cursor_img_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor_img, cursor_img_rect)
        else:
            pygame.mouse.set_visible(True)
            draw_text(screen, str(check_resaults(score)), center_x, 50)
        pygame.display.update()
        screen.fill(BLACK)


pygame.quit()

