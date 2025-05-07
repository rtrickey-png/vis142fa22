# skeleton code for project 2
# vis 142 fall 2022 
# This can take 20 minutes to hours to run.

# imports, don't change these but you can add imports you need
import pygame
from pygame.locals import *
from sys import exit
import random
import time
# record the start time
start_time = time.time()

#####################################################################
# We will be producing 4K video from an image sequence
# Important: you might want to work at lower resolution that fits, 
# your screens! Such as 1920 x 1080.
# And then change these back to 4096 × 2160 for production.
# On the other hand, you will have to deal with scaling issues if you do.
#####################################################################
width = 1920
height = 1080

#width = 4096 
#height = 2160 

#####################################################################
# Name and title, update to your name and title
#####################################################################
name = "Ryan Rickey"
title = "Leaves Falling in the Breeze" 

#####################################################################
# IMPORTANT - you will get your start sequence number from your TA
# If you use the default number 1000000 below, your work will not 
# be part of the class reel, as in every student must have different
# start sequence numbers.
#####################################################################
start_sequence_num = 5045000# CHANGE HERE

# Do not change these variables
# normal pygame stuff
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('generate 4K animation pngs')
frame_num = start_sequence_num
titles_font = pygame.font.SysFont(None, int(width/12)) # if name or title run off screen, try setting the literal to 16 instead of 12
name_f = titles_font.render(name, True, (255,255,255))
title_f = titles_font.render(title, True, (255,255,255))

# print resolution warning
if (width != 4096 and height != 2160):
    print("Warning: dimensions not 4K, be sure width and height are set to 4096 and 2160.")

# this function makes one second of black frames
def make_black():
    global frame_num
    screen.fill((0,0,0))
    pygame.display.update()
    for i in range(0, 60):
       pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
       frame_num = frame_num + 1
       clock.tick(60)
        
#############################################################
# this object is just for example purposes - Don't use this class
# unless of course to change it to be different from my circle foo
# using objects will make project 2 generally easier however

DEFAULT_IMAGE_SIZE = (100, 100)

class Chunk:
	loc_x = 0
	lox_y = 0
	skin = pygame.image.load('leaf.png')
	skin = pygame.transform.scale(skin, DEFAULT_IMAGE_SIZE)
	speed = 1
	xmult = 1
	ymult = 1
	stopped = 1
	alive = 1
	
	def __init__(self, loc_x, loc_y):
		self.loc_x = loc_x
		self.loc_y = loc_y
		
	def draw(self):
		screen.blit(self.skin, (self.loc_x, self.loc_y))
		self.update()
	
	def is_alive(self):
		if self.loc_y + DEFAULT_IMAGE_SIZE[0] >= height:
			self.alive = 0
			self.xmult = 0
			self.ymult = 0
		else:
			self.alive = 1

	def change_dir(self):
		change = random.randint(0, 500)
		if change >= 409:
			self.xmult = self.xmult * -1
	
	def update(self):
		if self.alive == 1 and self.stopped == 1:
			self.drop()
		elif self.alive == 1 and self.stopped == 0:
			dir = random.randint(0, 20)
			if(dir < 10):
				self.change_dir()
			self.is_alive()
			self.loc_x += 1.4 * self.xmult * self.alive
			self.loc_y += 0.8 * self.ymult * self.alive
	
	def drop(self):
		d = random.randint(0, 10000)
		if d >= 7000:
			self.stopped = 0
		else:
			self.stopped = 1

################################ end object
# this is the credits loop, which puts the title of your work
# and your name on the screen
make_black() # one second black
# produce title sequence
screen.fill((0,0,0))
screen.blit(name_f, (int(width/8), int(width/8)))
screen.blit(title_f, (int(width/8), int(width/4))) 
for i in range(0, 3*60):
    pygame.display.update()
    pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
    frame_num = frame_num + 1
    clock.tick(60)
make_black() # one second black
# set background image to tree
bg = pygame.image.load('tree_bg.png')

# make a list of active things
# active_circle_things = []
# for i in range (0, width + height):
#     active_circle_things.append(ActiveCircle())

leaves = []
num_leaves = random.randint(20, 50)
for i in range (0, 20):
	start_x = random.randint(49, 789)
	start_y = random.randint(289, 747)
	leaves.append(Chunk(height // 2 + start_x, width //2 - start_y))

# here is the main animation loop
for i in range(0, 20*60): # 20*60 frames is 20 seconds
    #########################################################
    # in the skeleton, your animation goes from here ########
    #########################################################
    screen.blit(bg, (0,0))
    for l in leaves:
         l.draw()
    #########################################################
    # to here ###############################################
    #########################################################

    # The next line can be commented out to speed up testing frame rate
    # by not writing the file. But for output to final frames,
    # you will need to ucomment it.
    pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
    frame_num = frame_num + 1
    pygame.display.update()
    clock.tick(60)

# print out stats
print("seconds:", int(time.time() - start_time))
print("~minutes: ", int((time.time() - start_time)/60))
# we just quit here
pygame.display.quit()
pygame.quit()
exit()

# you can make your files into a movie with ffmpeg:
# ffmpeg -r 60 -start_number 1000000 -s 4096x2160 -i %d.png -vcodec libx264 -crf 5 -pix_fmt yuv420p final.mp4
# with a few changes such as to start number, but this is just extra info here
