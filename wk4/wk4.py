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
	for w in range(len(imagedata) // 2): 
		r_len = random.randint(0, len(imagedata) // 2)
		# diff = len(imagedata) - r_len
		r_start = random.randint(0, len(imagedata) // 2 - r_len)
		if w < r_start:
			for k in range(3):
				row.append(random.randint(126,256) % 256)
		elif w >= r_start and w < (r_start + r_len):
			print(imagedata[h1][w*3:w*3+3])
			row.append(imagedata[h1][w*3] % 256)
			row.append(imagedata[h1][w*3+1] % 256)
			row.append(imagedata[h1][w*3+2] % 256)
		else:
			for k in range(3):
				row.append(random.randint(0,125) % 256)
	h1w1.append(row)
	# pad rest of line with random pixels
	# for w1 in range(len(imagedata[0]) // 2):
		#h1w1.append(imagedata[h1:w1+1])
# rand_slice = png.from_array(h1w1, 'RGB')
# rand_slice.save("test.png")
# rand_slice.show()
print(len(h1w1))
print(type(h1w1))
print(len(h1w1[0]))
print(type(h1w1[0][0]))
testpng = png.from_array(h1w1, 'RGB')
testpng.save("test.png")
# test = Image.fromarray(h1w1)
# test.save("test.png")
# h1_w1 = png.from_array(h1w1, 'RGB')
# print(h1_w1)
# h1_w1.save("h1_w1.png")


# imagadata is a list
#random.shuffle(imagedata)

# def swap_cols(np_arr, start_index, last_index):
    # print('start:%d end: %d' % (start_index, last_index))
    # np_arr[:, [start_index, last_index]] = np_arr[:, [last_index, start_index]]


# new_tree = png.from_array(imagedata, 'RGB')
# new_tree.save("new_tree.png")
# new_tree.show()
