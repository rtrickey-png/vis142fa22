# code from https://pythonguides.com/fractal-python-turtle/
from turtle import *
import turtle
import random
from PIL import Image

speed('fastest')

right(-90)
angle = 30 # randomize

def yaxis(size, lvl):
    if lvl > 0:
        angle = 30 + random.randint(0, 60)
        colormode(255)
        pencolor(60, 255, 0)
        forward(size)
        right(angle)
        yaxis(0.8 * size, lvl - 1)
        pencolor(0, 255 - (lvl * random.randint(1, 10)), 0)
        lt(2 * angle)
        yaxis(0.8 * size, lvl-1)
        pencolor(0, 255 - (lvl * random.randint(1, 10)), 0)
        right(angle)
        forward(-size)
yaxis(120, 5) # with lvl = 6 ~ 9 second. lvl = 5 ~ 5 seconds

# get canvas to save as a png
# https://stackoverflow.com/questions/35629520/convert-images-drawn-by-turtle-to-png-in-python 
cv = turtle.getcanvas()
cv.postscript(file='tree_1.eps', colormode='color')
img = Image.open('tree_1.eps')
img.save('tree_1.png', 'png')

turtle.done()
turtle.bye()
