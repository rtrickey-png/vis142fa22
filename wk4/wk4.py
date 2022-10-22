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

# imagadata is a list
random.shuffle(imagedata)

# def swap_cols(np_arr, start_index, last_index):
    # print('start:%d end: %d' % (start_index, last_index))
    # np_arr[:, [start_index, last_index]] = np_arr[:, [last_index, start_index]]


new_tree = png.from_array(imagedata, 'RGB')
new_tree.save("new_tree.png")
