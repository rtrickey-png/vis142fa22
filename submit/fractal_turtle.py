# code from https://pythonguides.com/fractal-python-turtle/
from turtle import *
import turtle

speed('fastest')

right(-90)
angle = 30

def yaxis(size, lvl):
    if lvl > 0:
        colormode(255)
        pencolor(255 // lvl**2, 255 // lvl, 255 // (lvl*3 % 255))
        forward(size)
        right(angle)
        yaxis(0.8 * size, lvl - 1)
        pencolor(0, 255 // lvl, 0)
        lt(2 * angle)
        yaxis(0.8 * size, lvl-1)
        pencolor(0, 255 // lvl, 0)
        right(angle)
        forward(-size)
yaxis(44, 10)
turtle.done()
