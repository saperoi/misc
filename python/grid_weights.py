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