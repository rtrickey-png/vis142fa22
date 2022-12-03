from PIL import Image
import numpy
from numpy import asarray
import random
import png
from Chunk import Chunk

image = Image.open('tree_1.png')

treedata = asarray(image)
print(treedata.shape)
# original input size

# arbitrary size of output
width = 1920
height = 1080

imagedata = []
transform = 0

# removed for now- flip a coin to blur image
# blur = random.randint(0, 1)
# if blur == 0:
# pad = random.randint(0, len(treedata[0])) % 100

# 1920 - 450 = 1470 / 2 = 735 pixels on either side
# 1080 - 512 = 568 / 2 = 284 pixels on top and bottom

l_bound = (width - len(treedata[0])) // 2
r_bound = l_bound + len(treedata[0])
t_bound = (height - len(treedata)) // 2
b_bound = t_bound + len(treedata)
 
# else reset pad in the loop
for h in range(height):
	row = []
	for w in range(width):
	# reset pad each iteration to create a blur effect
		# if blur == 1:
		# 	pad = random.randint(0, len(treedata[0])) % 100
		if w >= l_bound and h >= t_bound:
			if w < r_bound and h < b_bound:
				# print('h, w = %d, %d' %(h, w))
				# print('w-l, h-t : %d %d' %(w-l_bound, h-t_bound))
				# print(treedata[h - t_bound, w - l_bound])
				for x in treedata[h - t_bound, w - l_bound]:
					# if(h == 121):
					#	print(x)
					if x == 255:
						transform = h + random.randint(0, h //2)
					else:
						transform = 0
					row.append((x + transform) % 256)
				continue
		for i in range(3):
			row.append((h * random.randint(0, h // 2)) % 256)
	imagedata.append(row)
print(len(imagedata))
print(len(imagedata[0]))
print(len(imagedata[121]))

def round_dims(max_dim, start_dim, dim):
	if start_dim + dim > max_dim:
		return max_dim - start_dim
	return dim

# pick a random number of chunks
# was formerly at 111, like ten seconds on rbpi tho
num_chunks = random.randint(1, 55)
print('number of chunks: %d' %num_chunks)

chunks = []
for i in range(num_chunks):
    # get a random starting pixel for the height
	rh_start = random.randint(0, height)
    # get a random starting pixel for the width
	rw_start = random.randint(0, width * 3)
    # get a random height for the chunk
	r_height = random.randint(1, height // 4)
    # get a random width for the chunk
	r_width = random.randint(1, width * 3 // 4)

    # to prevent the random h and w from going out of bounds
	r_height = round_dims(height, rh_start, r_height)
	r_width = round_dims(width*3, rw_start, r_width)

    # add each chunk to a list
	chunks.append(Chunk(rh_start, rw_start, r_height, r_width))

# now iterate through chunks and draw them on top of imagedata
# change to only draw on top of tree
for chunk in chunks:
	for h in range(chunk.height):
		if h + chunk.h_start >= height: # safety
			break
		for w in range(chunk.width):
			if chunk.w_start + w >= width * 3 - 3: # safety
				break
			# flip a coin to decide whether to draw over imagedata
			transparent = random.randint(0, 1)
			if transparent == 1: # don't draw; continue
				w += 3
				continue
            # otherwise, draw!
			for p in range(3): # to change each R, G, B values
				# print('at [%d, %d]' %((chunk.h_start + h), (chunk.w_start + w)))
				val = random.randint(0, chunk.w_start // (chunk.h_start+1)) + h * w % 256
				# imagedata[chunk.h_start + h][chunk.w_start + w + p] = random.randint(0, 255)

# save image
chunkpng = png.from_array(imagedata, 'RGB').save('rickey_out3.png')
