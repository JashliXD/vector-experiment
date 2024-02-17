import pygame
from math import *
from vector import Vector

pygame.init()

win = pygame.display.set_mode((1200,600))

class Entity:
    def __init__(self, x,y):
        self.vector = Vector(x,y)
        
        self.target = None
        self.angle = None
    
    def draw(self):
        size = 30
        offset = size/2
        pygame.draw.rect(win, (255,255,255), (self.vector.x-offset,self.vector.y-offset,size,size))
        if self.target:
            pygame.draw.line(win, (255,0,255), (self.vector.x,self.vector.y), (self.target.x,self.target.y), 3)
    
    def shoot(self, pos):
        self.target = Vector(pos[0], pos[1])
        self.angle = self.vector.get_angle(self.target.get_pos())

        if self.vector.get_distance(self.target.get_pos()) < 1:
            self.target = None
            self.angle = None
    def update(self):
        if self.target:
            self.vector.x += cos(self.angle)
            self.vector.y += sin(self.angle)
            if self.vector.get_distance(self.target.get_pos()) < 1:
                self.target = None
                self.angle = None
        self.draw()
    

test = Entity(600,300)

mouse = pygame.mouse

run = True
while run:
    win.fill((0,0,0))
    test.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if mouse.get_pressed()[0]:
        test.shoot(mouse.get_pos())
    #print(test.get_angle(mouse.get_pos()))

    pygame.display.update()