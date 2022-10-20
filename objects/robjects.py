# on the way to better

import pygame
from pygame.locals import *
from sys import exit
import math
import random

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('objects!')


class Face:
    color = (15,15,15)
    happy = False
    locationX = 0
    locationY = 0
    expressionStart = 0
    expressionEnd = 0
    size = 50
    fill = 0
    black = (0,0,0)
    xmult = 1
    ymult = 1

    def __init__(self, color, happy, locationX, locationY):
        self.color = color
        self.happy = happy
        self.locationX = locationX
        self.locationY = locationY
        if happy:
            self.expressionStart = self.degreesToRadians(180)
            self.expressionEnd = self.degreesToRadians(360)
        else: # sad
            self.expressionStart = self.degreesToRadians(0)
            self.expressionEnd = self.degreesToRadians(180)

    def draw(self):
        pygame.draw.circle(screen, self.color, \
            (self.locationX, self.locationY), self.size, self.fill)
        pygame.draw.circle(screen, self.black, \
                (self.locationX - 10, self.locationY - 10), 10, 0)
        pygame.draw.circle(screen, self.black, \
                (self.locationX+ 20 , self.locationY - 10), 10, 0)
        if self.happy == False:
            pygame.draw.arc(screen, self.black, \
                (self.locationX - 20, self.locationY + 20, 40, 40), \
                            self.expressionStart, self.expressionEnd, 5)
        else:
            pygame.draw.arc(screen, self.black, \
                (self.locationX - 20, self.locationY - 10, 40, 40), \
                            self.expressionStart, self.expressionEnd, 5)

    def update(self):
        self.reflect()
        self.locationX += 1 * self.xmult
        self.locationY += 1 * self.ymult

    def changeMood(self):
        # Can we add features? How would we do that?
        pass
        

    # degrees to radians
    def degreesToRadians(self, deg):
        return deg/180.0 * math.pi
   
    # idea: make a function to reflect image when at a boundary
    def reflect(self):
        if self.at_top_edge():
            self.ymult *= -1
        if self.at_bot_edge():
            self.ymult *= -1
        if self.at_left_edge():
            self.xmult *= -1
        if self.at_right_edge():
            self.xmult *= -1

    def at_top_edge(self):
        if self.locationY - self.size <= 0:
            return 1
        return 0

    def at_right_edge(self):
        if self.locationX  + self.size>= 640:    
            return 1
        return 0
    
    def at_bot_edge(self):
        if self.locationY  + self.size>= 480:
            return 1
        return 0
    def at_left_edge(self):
            if self.locationX  - self.size<= 0:
                return 1
            return 0

# make list of faces!
faces = [Face((255,255,0), False, 100, 100), Face((0,255,255), True, 300, 300)]
for i in range(100):
    ri = random.randint(0,255)
    gi = random.randint(0,255)
    bi = random.randint(0,255)
    hapsad = random.randint(0,1)
    xi = random.randint(40, 600)
    yi = random.randint(40,444)
    face_i = Face((ri, gi, bi), hapsad, xi, yi)
    faces.append(face_i)
                        
while True:
    for event in pygame.event.get():
        #print(event.type, QUIT)
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()

    screen.fill((0,0,0))

    #i = 0 # this counter var is not longer needed
    for face in faces:
        face.draw()
        face.update()
    pygame.display.update()
    clock.tick(30)


