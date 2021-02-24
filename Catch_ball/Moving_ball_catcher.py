import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 18
SIZE_X = 1200
SIZE_Y = 900
game_speed = 10
game_time = 5

screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
right = screen.get_rect().right
left = screen.get_rect().left
top = screen.get_rect().top
bottom = screen.get_rect().bottom
center_x = screen.get_rect().centerx
center = screen.get_rect().center

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
        step = randint(-game_speed, game_speed)

    if step < 0:
        step = randint(game_speed//2, game_speed)
    else:
        step = randint(-game_speed, -game_speed//2)
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

def update_winners(score, input_box_text):
    WIN = []    
    with open('winners.txt', 'r') as win:
        WIN = win.readlines()                
        for player in WIN:
            points = int(player[0:player.rindex(',')])            
            if points < score:
                WIN[WIN.index(player)] = str(score)+', '+str(input_box_text)+'\n'
                break            
        WIN.append(str(score)+', '+input_box_text)
    with open('winners.txt', 'w') as win:
        for player in WIN:
            win.write(player)
    return WIN
    
if __name__ == '__main__':
    pygame.display.update()
    clock = pygame.time.Clock()
    balls_creation()
    score = 0
    finished = False
    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load('cursor_img.png')
    cursor_img_rect = cursor_img.get_rect()
    input_box = pygame.Rect(center, (100, 32))
    input_box_active = False
    input_box_text = 'Your name'
    winner_input = False

    while not finished:
        clock.tick(FPS)
        seconds = game_time - (pygame.time.get_ticks())//1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:            
                score = hit_counter(score, event.pos)                
            elif event.type == pygame.KEYDOWN:
                if input_box_active:
                    if event.key == pygame.K_RETURN:
                        winner_input = True
                        update_winners(score, input_box_text)
                    elif event.key == pygame.K_BACKSPACE:
                        input_box_text = input_box_text[:-1]
                    else:
                        input_box_text += event.unicode              
        
        if seconds > 0:           
            draw_text(screen,
                      'Hits - '+str(score)+'  ('+str(seconds)+')',
                      center_x, 25)
            new_ball()
            coords_update()
            cursor_img_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor_img, cursor_img_rect)            
        elif not winner_input and score > 0:
            A = []
            pygame.mouse.set_visible(True)            
            input_box_active = True
            font = pygame.font.Font(font_name, 20)
            txt_surface = font.render(input_box_text, True, WHITE)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))            
            rect(screen, BLUE, input_box, 2)            
        else:                        
            with open('winners.txt', 'r') as win:
                draw_text(screen, win.read(), center_x, 50)
        pygame.display.update()
        screen.fill(BLACK)

pygame.quit()
