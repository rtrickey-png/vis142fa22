from PIL import Image
import numpy
from numpy import asarray
import random
import png
from Chunk import Chunk

image = Image.open('fractal-tree1.png')

treedata = asarray(image)
print(treedata.shape)
# np_img = numpy.array(image)
# pil_img = Image.fromarray(np_img)

# TODO: try getting to 300 x 300
width = 300
height = 300

imagedata = []
transform = 0
for h in range(height):
    row = []
    for w in range(width):
        for x in treedata[h,(w+130),:3]:
            if x == 0:
                transform = h + random.randint(0, h //2)
            row.append((x + transform) % 256)
    imagedata.append(row)

def round_dims(max_dim, start_dim, dim):
	if start_dim + dim > max_dim:
		return max_dim - start_dim
	return dim

# pick a random number of chunks
num_chunks = random.randint(1, 111)
print('number of chunks: %d' %num_chunks)
# for each chunk, decide its dimensions at random
chunks = []
for i in range(num_chunks):
	rh_start = random.randint(0, height)
	rw_start = random.randint(0, width * 3)
	r_height = random.randint(1, height // 4)
	r_width = random.randint(1, width * 3 // 4)
	# need to check that start + h/w are within bounds
	r_height = round_dims(height, rh_start, r_height)
	r_width = round_dims(width*3, rw_start, r_width)
	chunks.append(Chunk(rh_start, rw_start, r_height, r_width))

# now iterate through chunks and draw them on top of imagedata
for chunk in chunks:
	for h in range(chunk.height):
	 	# print(h)
		if h + chunk.h_start >= height:
			break
		for w in range(chunk.width):
			# print(w)
			if chunk.w_start + w >= width * 3 - 3:
				break
			# flip a coin
			transparent = random.randint(0, 1)
			if transparent == 1:
				w += 3
				continue
			for p in range(3):
				# print('at [%d, %d]' %((chunk.h_start + h), (chunk.w_start + w)))
				val = random.randint(0, chunk.w_start // chunk.h_start) + h * w % 256	
				imagedata[chunk.h_start + h][chunk.w_start + w + p] = random.randint(0, 255)
				# else do nothing
chunkpng = png.from_array(imagedata, 'RGB').save('chunkpng3.png')


# now try to randomize squares
# 4 square method
h1w1 = []
# idea, fill rest of randomly chosen data from image with random colors
for h1 in range(len(imagedata) // 2):
	row = []
	for w in range(len(imagedata) // 3): 
		r_len = random.randint(0, len(imagedata) // 2)
		# diff = len(imagedata) - r_len
		r_start = random.randint(0, len(imagedata) // 2 - r_len)
		if w < r_start:
			for k in range(3):
				imagedata[h1][w+k] = 0
				# row.append(random.randint(126,256) % 256)
		#elif w >= r_start and w < (r_start + r_len):
			
			# print(imagedata[h1][w*3:w*3+3])
			# row.append(imagedata[h1][w*3] % 256)
			# row.append(imagedata[h1][w*3+1] % 256)
			# row.append(imagedata[h1][w*3+2] % 256)
		elif w >= (r_start + r_len):
			for k in range(3):
				imagedata[h1][w+k] = 255
				# row.append(random.randint(0,125) % 256)
	# h1w1.append(row)
	# imagedata[h1] = row
# h1w1_arr = asarray(h1w1)
# imagedata_arr = asarray(imagedata)
		
# print(len(h1w1))
# print(type(h1w1))
# print(len(h1w1[0]))
# print(type(h1w1[0][0]))
testpng = png.from_array(imagedata, 'RGB')
testpng.save("test.png")


#random.shuffle(imagedata)

