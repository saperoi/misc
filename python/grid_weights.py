import random
import json
from PIL import Image
import os

methodchoice = "gray"


grid = open("tests/weights.json", "w")
grid.write("")
grid.close()
grid = open("tests/weights.json", "a")

horiz = random.randint(8, 27)
vert = random.randint(8, 27)

grid.write("{\n")

for i in range(horiz):
    i = str(i)
    grid.write("\t\"" + i + "\": {\n")
    for j in range(vert):
        j = str(j)
        weight = str(random.randint(0, 255))
        if int(j) == vert - 1:
            grid.write("\t\t\"" + j +"\": " + weight + "\n")
        else:
            grid.write("\t\t\"" + j +"\": " + weight + ",\n")
    if int(i) == horiz - 1:
        grid.write("\t}\n")
    else:
        grid.write("\t},\n")

grid.write("}")
grid.close()

weight = open("tests/weights.json", "r")
weights = json.loads(weight.read())
weight.close()

bw = open("tests/bw.json", "w")
bw.write("")
bw.close()
bw = open("tests/bw.json", "a")

bw.write("{\n")

for i in range(horiz):
    i = str(i)
    bw.write("\t\"" + i + "\": {\n")
    for j in range(vert):
        j = str(j)
        if weights[i][j] < 256/2:
            cc = "0"
        else:
            cc = "1"
        if int(j) == vert - 1:
            bw.write("\t\t\"" + j +"\": " + cc + "\n")
        else:
            bw.write("\t\t\"" + j +"\": " + cc + ",\n")
    if int(i) == horiz - 1:
        bw.write("\t}\n")
    else:
        bw.write("\t},\n")

bw.write("}")
bw.close()

bw = open("tests/bw.json", "r")
cs = json.loads(bw.read())
bw.close()

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
            if cs[i][j] == 0:
                im.putpixel((x, y), hc0)
            if cs[i][j] == 1:
                im.putpixel((x, y), hc1)
if methodchoice == "gray":
    for i in range(horiz):
        for j in range(vert):
            x = int(i)
            y = int(j)
            i = str(i)
            j = str(j)
            r = weights[i][j]
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
im = im.resize(size, resample=Image.NEAREST)
im.save("./tests/10x/" + name + '.png')