
#图形用户界面和游戏开发

import tkinter
import tkinter.messagebox

def main():
  flag = True

  def change_label_text():
    nonlocal flag
    flag = not flag
    color, msg = ('red', 'Hello, world!')\
      if flag else ('blue', 'Goodbye, world!')
    label.config(text=msg, fg=color)

  def confirm_to_quit():
    if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
      top.quit()

  top = tkinter.Tk()
  top.geometry('240x160')
  top.title('小游戏')
  label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
  label.pack(expand=1)
  panel = tkinter.Frame(top)
  button1 = tkinter.Button(panel, text='修改', command=change_label_text)
  button1.pack(side='left')
  button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
  button2.pack(side='right')
  panel.pack(side='bottom')
  tkinter.mainloop()

if __name__ == '__main__':
  main()
  

class Wechat(object):
    def __init__(self, title, content, sender, receiver, time):
        self._title = title
        self._content = content
        self._sender = sender
        self._receiver = receiver
        self._time = time
   
    def quit(self):
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            self._top.quit()

    def change_label_text(self):
        color, msg = ('red', 'Hello, world!') if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    def create_wechat(self):
        top = tkinter.Tk()
        self._top = top
        top.geometry('240x160')
        top.title(self._title)
        label = tkinter.Label(top, text=self._content, font='Arial -32', fg='red')
        label.pack(expand=1)
        panel = tkinter.Frame(top)
        button1 = tkinter.Button(panel, text='修改', command=self.change_label_text)
        button1.pack(side='left')
        button2 = tkinter.Button(panel, text='退出', command=self.quit)
        button2.pack(side='right')
        panel.pack(side='bottom')
        tkinter.mainloop()

def main():
    wechat = Wechat('微信', 'Hello, world!', '张三', '李四', '2019-01-01')
    wechat.create_wechat()
  

if __name__ == '__main__':
  main()
      
# 使用Pygame进行游戏开发

import pygame
def main():
  pygame.init()
  screen = pygame.display.set_mode((800, 600))
  pygame.display.set_caption('大球吃小球')
  running = True
  
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

if __name__ == '__main__':
  main()

# 在窗口中绘图

import pygame
def main():
  pygame.init()
  screen = pygame.display.set_mode((800, 600))
  pygame.display.set_caption('大球吃小球')
  screen.fill((242, 242, 242))
  pygame.draw.circle(screen, (255, 0, 0,), (100, 100), 30, 0)
  pygame.display.flip()
  running = True
  
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

if __name__ == '__main__':
  main()

# 加载图像
import pygame

def main():
  pygame.init()
  screen = pygame.display.set_mode((800, 600))
  pygame.display.set_caption('大球吃小球')
  screen.fill((242, 242, 242))
  ball_image = pygame.image.load('./res/woman-695456_1280.jpg')
  screen.blit(ball_image, (50, 50))
  pygame.display.flip()
  running = True
  
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

if __name__ == '__main__':
  main() 


# 实现动画效果

import pygame

def main():
  pygame.init()
  screen = pygame.display.set_mode((800, 600))
  pygame.display.set_caption('大球吃小球')
  x, y = 50, 50
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    screen.fill((242, 242, 242))
    pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
    pygame.display.flip()
    pygame.time.delay(10)
    x, y = x + 1, y + 1
    if x >= 750 or y <= 50:
      x, y = 50, 50

if __name__ == '__main__':
  main()

from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    """颜色"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)

# 事件处理
# import pygame
def main():
  
  balls = []
  pygame.init()
  screen = pygame.display.set_mode((800, 600))
  pygame.display.set_caption('大球吃小球11')
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x, y = event.pos
        radius = randint(10, 100)
        sx, sy = randint(-10, 10), randint(-10, 10)
        color = Color.random_color()
        ball = Ball(x, y, radius, sx, sy, color)
        balls.append(ball)
    screen.fill((255, 255, 255))
    for ball in balls:
      if ball.alive:
        ball.draw(screen)
      else:
        balls.remove(ball)
    pygame.display.flip()
    pygame.time.delay(50) 
    for ball in balls:
      ball.move(screen)
      for other in balls:
        ball.eat(other)


if __name__ == '__main__': 
  main()

