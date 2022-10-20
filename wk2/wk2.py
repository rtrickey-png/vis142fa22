import numpy as np
import png

pngWriter = png.Writer(357, 222)
reader = png.Reader(filename="doggo.png")

# read returns a 4-tuple with (width, height, rows, info)
# asDirect returns a 4 tuple too, but we will give the row iterator to numpy to manipulate.

# [2] pulls out rows from reader.asDirect()
#print(reader.asDirect()[2])
l =list(reader.read())
print(l[2])
doggo_arr = np.vstack(map(np.uint8, reader.asDirect()[2]))

# pngWriter.write("ndoggo.png", doggo)

#manipulate array
doggo_copy = doggo_arr.copy()

print(len(doggo_copy[0]))
print((doggo_copy[0]))
print(doggo_copy[0])
print(len(doggo_copy))

for i in range(len(doggo_copy)):
    for j in range(len(doggo_copy[i])):
        if j % 4 == 0:
            continue
        if doggo_copy[i][j] == 255:
            doggo_copy[i][j] = 55 
            #doggo_copy[i][j] = doggo_copy[i][j] + 27

# I am leaving with with figuring out how the numpy array holds the image data. I want to access the white pixels but I keep messing with the alpha variables apparently.
png.from_array(doggo_copy, mode="RGBA").save("ndoggo.png")
