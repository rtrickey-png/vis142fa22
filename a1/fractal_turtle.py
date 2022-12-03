# code from https://pythonguides.com/fractal-python-turtle/
from turtle import *
import turtle
import random
from PIL import Image

speed('fastest')

# print(turtle.pos())
penup()
turtle.goto(pos()[0], pos()[1]-400)
pendown()

right(-90)
angle = 30 # randomize
trunk = 8
width(7)

def yaxis(size, lvl):
	if lvl > 0:
		colormode(255)
		width(lvl + 3)
		# if lvl == trunk or lvl == 1:
		# 	pencolor(133, 60, 15)
		angle = 30 + random.randint(0, 60)
		pencolor(133, 60 + lvl * random.randint(0, 14), 15)
		if lvl == trunk:
			forward(size * 2)
		else:
			forward(size)
		right(angle)
		yaxis(0.8 * size, lvl - 1)
		# pencolor(0, 255 - (lvl * random.randint(1, 10)), 0)
		lt(2 * angle)
		yaxis(0.8 * size, lvl-1)
		# pencolor(0, 255 - (lvl * random.randint(1, 10)), 0)
		right(angle)
		if lvl == trunk:
			forward(-size * 2)
		else:
			forward(-size)
yaxis(150, trunk) # with lvl = 6 ~ 9 second. lvl = 5 ~ 5 seconds

# get canvas to save as a png
# https://stackoverflow.com/questions/35629520/convert-images-drawn-by-turtle-to-png-in-python 
cv = turtle.getcanvas()
cv.postscript(file='tree_1.eps', colormode='color')
img = Image.open('tree_1.eps')
img.save('tree_1.png', 'png')

turtle.done()
turtle.bye()
