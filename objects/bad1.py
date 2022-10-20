#just terrible

import pygame
from pygame.locals import *
from sys import exit
import math

# declare face 1 variables
colorR1 = 255
colorG1 = 255
colorB1 = 0
happy1 = False
locationX1 = 100
locationY1 = 100

# declare face 2 variables
colorR2 = 0
colorG2 = 255
colorB2 = 255
happy2 = True
locationX2 = 300
locationY2 = 300

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('bad')

black = (0,0,0)

# degrees to radians
def degreesToRadians(deg):
    return deg/180.0 * math.pi

startSad = degreesToRadians(0)
endSad = degreesToRadians(180)
startHappy = degreesToRadians(180)
endHappy = degreesToRadians(360)

# event/animation loop                        
while True:
    for event in pygame.event.get():
        #print(event.type, QUIT)
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()

    screen.fill(black)

    pygame.draw.circle(screen, (colorR1,colorG1,colorB1), \
        (locationX1, locationY1), 50, 0)
    # look at the sequentially named
    # variables and "hard coded" literal values
    # usually a bad sign!!!
    pygame.draw.circle(screen, black, \
                       (locationX1 - 10, locationY1 - 10), 10, 0)   
    pygame.draw.circle(screen, (black), \
                       (locationX1+ 20 , locationY1 - 10), 10, 0)   
    pygame.draw.arc(screen, black, \
                        (locationX1 - 20, locationY1 + 20, 40, 40), startSad, endSad,5)
    locationX1+=1
    locationY1+=1
    # draw the second one
    pygame.draw.circle(screen, (colorR2,colorG2,colorB2), \
        (locationX2, locationY2), 50, 0)
    pygame.draw.circle(screen, black, \
                       (locationX2 - 10, locationY2 - 10), 10, 0)
    pygame.draw.circle(screen, (black), \
                       (locationX2+ 20 , locationY2 - 10), 10, 0)
    pygame.draw.arc(screen, black, \
                        (locationX2 - 20, locationY2 - 10, 40, 40), startHappy, endHappy,5)
    locationX2+=1
    locationY2+=1    
 
    pygame.display.update()
    clock.tick(30)


