from PIL import Image
import os
import random
import math

strr = "2935955605"
vert = int(strr[-2:])
deck = int(strr[:-2])
binn = str(bin(int(deck))[2:])
horiz = math.ceil(len(binn)/vert)

hc0 = (0, 0, 0)
hc1 = (255, 255, 255)
im = Image.new(mode="RGB", size=(horiz, vert))

for j in range(vert):
    for i in range(horiz):
        x = horiz - int(i) -1
        y = vert - int(j) -1
        print(x, y)
        try:
            k = j*vert + i
            char = int(str(binn)[::-1][k])
        except:
            char = 1
        if char == 0:
            im.putpixel((x, y), hc0)
        if char == 1:
            im.putpixel((x, y), hc1)

namea = [random.choice('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890') for _ in range(10)]
name = ""
for i in range(len(namea)):
    name += namea[i]
im.save("./tests/" + "f" + '.png')
