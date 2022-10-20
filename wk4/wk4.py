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
        #i = 0
        for x in treedata[h,(w+130),:3]:
            #if i == 2:
            #   continue
            if x == 0:
                transform = h
            row.append((x + transform) % 256)
            # i+=1
    imagedata.append(row)


# now try to transform chunks
# for h in range(height):
#     for w in range(width):

np_imagedata = numpy.array(imagedata)

def swap_cols(np_arr, start_index, last_index):
    # print('start:%d end: %d' % (start_index, last_index))
    np_arr[:, [start_index, last_index]] = np_arr[:, [last_index, start_index]]


for i in range (width):
    swap_cols(np_imagedata, (random.randint(0, width)), (random.randint(0,width)))
imagedata = list(np_imagedata)
new_tree = png.fromarray(np_imagedata, 'RGB')
new_tree.save("new_tree.png")
