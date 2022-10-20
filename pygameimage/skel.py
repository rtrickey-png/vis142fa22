# this example contains all of the basic dance moves to create an animation
# including importing and blitting images 

# to use pygame, you might need to install pygame!
# sudo apt-get install python3-pygame
# or
# pip3 install pygame
# but some distros will come with it

import pygame
from pygame.locals import *
import math

width = 640
height = 480

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('drawing to file')
                        
screen.fill((0,0,0))
pygame.draw.circle(screen, (0, 0, 255), (width/4, height/4), width/6)
pygame.draw.polygon(screen, (0, 255, 0), [(400, 80), (500, 160), (300, 160)], 10)
for num in range(50, 256):
    pygame.draw.rect(screen, (num, 0, 0), Rect(width/3 + num, height/3 + num, width/10, height/10), 0) 
     
pygame.display.update()
pygame.image.save(screen, "drawn.png")
pygame.display.quit()
pygame.quit()
exit()


