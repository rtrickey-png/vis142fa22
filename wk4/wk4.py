from PIL import Image
import numpy
from numpy import asarray
import random
import png

image = Image.open('fractal-tree1.png')

treedata = asarray(image)
print(treedata.shape)
# np_img = numpy.array(image)
# pil_img = Image.fromarray(np_img)

width = 255
height = 255

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

print(len(imagedata)) # 255
print(type(imagedata))
print(len(imagedata[0])) # 255 * 3
print(type(imagedata[0]))
print(type(imagedata[0][0]))
# print(imagedata[0])

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

