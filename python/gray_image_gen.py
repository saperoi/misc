from PIL import Image
import random

horiz = 8
vert = 8

methodchoice = "bw"

hc0 = (0, 0, 0)
hc1 = (255, 255, 255)
im = Image.new(mode="RGB", size=(horiz, vert))

if methodchoice == "bw":
    for i in range(horiz):
        for j in range(vert):
            x = int(i)
            y = int(j)
            i = str(i)
            j = str(j)
            cs = random.randint(0, 1)
            if cs == 0:
                im.putpixel((x, y), hc0)
            if cs == 1:
                im.putpixel((x, y), hc1)
if methodchoice == "gray":
    for i in range(horiz):
        for j in range(vert):
            x = int(i)
            y = int(j)
            r = random.randint(0, 255)
            cm = (r, r, r)
            im.putpixel((x, y), cm)

k = 250
width = horiz * k
height = vert * k
size = (width, height)
#im.show()
namea = [random.choice('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890') for _ in range(10)]
name = ""
for i in range(len(namea)):
    name += namea[i]
im.save("./tests/" + name + '.png')
"""
im = im.resize(size, resample=Image.NEAREST)
im.save("./tests/10x/" + name + '.png')
"""