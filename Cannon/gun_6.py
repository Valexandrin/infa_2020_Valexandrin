from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball:
    def __init__(self, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.g = 1
        self.dt = 2
        self.color = choice(['blue', 'green', 'red', 'brown'])
        
    def set_shape(self):
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill = self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть,
        обновляет значения self.x и self.y с учетом скоростей self.vx и self.vy,
        силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """        
        
        if self.x + self.r > 800:
            self.vx *= -1
        if self.y + self.r > 550:       
            self.vy *= -0.65
        self.x += self.vx
        self.y -= self.vy*self.dt - self.g*self.dt**2/2        
        self.vy -= self.dt*self.g        
        self.vy *= 0.95
        self.vx *= 0.94
        self.dt *= 0.99        
        self.set_coords()
                    
    def hide(self):
        """Исчезновение остановившегося шарика."""        
        if abs(self.vx) < 0.5 and abs(self.vy) < 0.5:            
            #canv.delete(self.id)
            canv.coords(self.id, -10, -10, -10, -10)            
            
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью,
            описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели.
            В противном случае возвращает False.
        """        
        dist = ((self.x - obj.x)**2 + (self.y - obj.y)**2) ** (1/2)
        if dist < self.r + obj.r:
            return True        
        return False


class hexagon(ball):
    def __init__(self, x, y):
        """ Конструктор класса hexagon

        Args:
        x - начальное положение снаряда по горизонтали
        y - начальное положение снаряда по вертикали
        """
        super().__init__(x, y)
        
    def set_shape(self):
        self.id = canv.create_polygon(
                self.x - self.r, self.y + self.r/2,
                self.x - self.r, self.y - self.r/2,
                self.x, self.y - self.r,
                self.x + self.r, self.y - self.r/2,
                self.x + self.r, self.y + self.r/2,
                self.x, self.y + self.r,
                fill = self.color
        )
    
    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r, self.y + self.r/2,
                self.x - self.r, self.y - self.r/2,
                self.x, self.y - self.r,
                self.x + self.r, self.y - self.r/2,
                self.x + self.r, self.y + self.r/2,
                self.x, self.y + self.r
        )


class gun():
    def __init__(self):
        self.f2_power = 30
        self.f2_on = 0
        self.an = 1
        self.x = 400
        self.y = 500
        self.r = 100        
        self.id = canv.create_line(self.x, self.y,
                                   self.x + self.r, self.y - self.r,
                                   tags="Tank", width=10)
        self.oval = canv.create_oval(self.x - self.r/2, self.y + self.r/4,
                                     self.x + self.r/2, self.y - self.r/4,
                                     tags="Tank", fill = "black")
        self.base = canv.create_polygon(
            self.x - self.r*4/5, self.y + self.r/5,
            self.x - self.r, self.y + self.r*2/5,
            self.x - self.r*2/3, self.y + self.r*2/3,
            self.x + self.r*2/3, self.y + self.r*2/3,
            self.x + self.r, self.y + self.r*2/5,
            self.x + self.r*4/5, self.y + self.r/5,
            tags="Tank", fill = "black")
        self.pow = canv.create_line(self.x, self.y + self.r*2/3,
                                    self.x, self.y + self.r*1/4,
                                    tags="Tank", fill = "orange", width=10)
        
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от
        положения мыши.
        """
        global balls, bullet        
        bullet += 1                
        new_ball = create_gameitem(ball(self.x, self.y), hexagon(self.x, self.y))
        new_ball.set_shape()                       
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        if self.an < 1.6 and self.an > -1.5 and event.x-self.x < 0:
            self.an = - 1.5
        if self.an < 1.6 and self.an > 0 and event.x-self.x > 0:
            self.an = 0
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 30

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:            
            self.an = math.atan((event.y-self.y) / (event.x-self.x))
            if self.an < 1.6 and self.an > -1.5 and event.x-self.x < 0:
                self.an = - 1.5
            if self.an < 1.6 and self.an > 0 and event.x-self.x > 0:
                self.an = 0
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, self.r) * math.cos(self.an),
                    self.y + max(self.f2_power, self.r) * math.sin(self.an))
        canv.coords(self.pow, self.x, self.y + self.r*2/3,
                     self.x, self.y + self.r*2/3 - max(self.f2_power, 10)/1.5)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1

    def moving(self, event):
        if event.keysym == 'Right':
            canv.move("Tank", 5, 0)
            self.x += 5
        if event.keysym == 'Left':
            canv.move("Tank", -5, 0)
            self.x -= 5


class target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(50, 750)
        y = self.y = rnd(50, 300)
        r = self.r = rnd(5, 50)
        self.vx = rnd(1, 10)
        self.vy = rnd(1, 10)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)

    def set_coords(self):
        canv.coords(self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        if self.x + self.vx + self.r > 800 or self.x - abs(self.vx) - self.r < 0:
            self.vx *= -1
        if self.y + self.vy + self.r > 450 or self.y - abs(self.vy) - self.r < 0:       
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy
        self.set_coords()       


class plane(target):
    def __init__(self):
        super().__init__()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = 60
        y = self.y = rnd(50, 250)
        r = self.r = rnd(20, 50)        
        self.vx = rnd(1, 10)
        self.vy = 0
        color = self.color = 'blue'
        canv.coords(self.id, x-r, y-r/2, x+r, y+r/2)
        canv.itemconfig(self.id, fill=color)

    def set_coords(self):
        canv.coords(self.id,
                self.x - self.r,
                self.y - self.r/2,
                self.x + self.r,
                self.y + self.r/2
        )


def create_gameitem(var_1, var_2):
    name = [var_1, var_2]        
    new_item = name[rnd(0, len(name))]
    return new_item
        

targets = []
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
points = 0
counter = canv.create_text(30,30,text = points,font = '28')

def new_game(event=''):
    
    global gun, targets, screen1, balls, bullet, points 
    for t in range(5):
        t = create_gameitem(plane(), target())
        t.new_target()
        targets += [t]    
    targets_live = 1    
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    root.bind('<KeyPress>', g1.moving)     
    canv.itemconfig(screen1, text='')
    while targets or balls:
        bl = ball(500, 500)
        for t in targets:
            t.move()
        for b in balls:
            b.move()                
            for t in targets:                
                if b.hittest(t):
                    t.hit()                    
                    points += 1
                    canv.itemconfig(counter, text=points)
                    targets.remove(t)                    
            if not targets and targets_live:               
                targets_live = 0                
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' +
                                str(bullet) + ' выстрелов')                                
                root.after(3500, new_game)       
            b.hide()                        
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()  
        canv.delete(gun)
    
new_game()

mainloop()
