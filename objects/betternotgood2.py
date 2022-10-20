#less terrible

import pygame
from pygame.locals import *
from sys import exit
import math

# parallel lists - something still wrong but bear with me
colorR = []
colorG = []
colorB = []
happy = []
locationX = []
locationY = []

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('parallel')

black = (0,0,0)

# make two faces
colorR.append(255)
colorG.append(255)
colorB.append(0)
happy.append(False)
locationX.append(100)
locationY.append(100)

colorR.append(0) # so now, colorR is equal to [255, 0], etc
colorG.append(255)
colorB.append(255)
happy.append(True)
locationX.append(300)
locationY.append(300)

# degrees to radians
def degreesToRadians(deg):
    return deg/180.0 * math.pi

startSad = degreesToRadians(0)
endSad = degreesToRadians(180)
startHappy = degreesToRadians(180)
endHappy = degreesToRadians(360)

                        
while True:
    for event in pygame.event.get():
        #print(event.type, QUIT)
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()

    screen.fill(black)

    # the for statment is not exactly right here, enumerate would be better python
    i = 0
    for val in colorR:
        pygame.draw.circle(screen, (colorR[i],colorG[i],colorB[i]), \
            (locationX[i], locationY[i]), 50, 0)
        pygame.draw.circle(screen, black, \
                           (locationX[i] - 10, locationY[i] - 10), 10, 0)
        pygame.draw.circle(screen, (black), \
                           (locationX[i]+ 20 , locationY[i] - 10), 10, 0)
        if happy[i] == False:
            pygame.draw.arc(screen, black, \
                            (locationX[i] - 20, locationY[i] + 20, 40, 40), startSad, endSad,5)
        else:
            pygame.draw.arc(screen, black, \
                            (locationX[i] - 20, locationY[i] - 10, 40, 40), startHappy, endHappy,5)
        locationX[i]+=1
        locationY[i]+=1
        i+=1
    pygame.display.update()
    clock.tick(30)


