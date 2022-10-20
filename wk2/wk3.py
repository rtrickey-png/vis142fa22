from PIL import Image
import numpy
from numpy import asarray
import random
import png

image = Image.open('super-mario-bros.jpg')

mariodata = asarray(image)
# alertnatively,
np_img = numpy.array(image)
# print(type(numpydata))
# print(np_img.shape)

# print(image.format)
# print(image.size)
# print(image.mode)
pil_img = Image.fromarray(np_img)
# print(type(pil_img))
# print(np_img)
# print(pil_img.mode)
# print(pil_img.size)

width = 980
height = 653

imagedata = []
for h in range(height):
    row = []
    for w in range(width):
        for x in mariodata[h,w]:
            # print(x) # 161 and 174
            #if x != 161:
            #    x = 0
            #if x != 174: 
            #    x = 0
            row.append(x)
        # if row[w] == 161:
        #    if row[w+1]
        # if w % 3 == 1:
        #    row[w] = 174
        # if w % 3 == 2:
        #    row[w] = 253
    imagedata.append(row)

new_bros = png.fromarray(imagedata, 'RGB')
new_bros.save("new_bros.png")
