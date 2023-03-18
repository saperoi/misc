from PIL import Image
import binascii
import random
import math

plain = str(input("Text to encode: "))
asciirr = []
for i in list(plain):
    k = str(bin(ord(i)))[2:]
    while len(k) < 8:
        k = "0" + k
    asciirr.append(k)

asciirr = list(" ".join(asciirr))
u = 10
lent = len(asciirr)*u

im = Image.new(mode="RGB", size=(lent, lent))

for j in range(lent):
    for i in range(lent):
        x = lent - int(j) -1
        y = lent - int(i) -1
        k = math.floor((j)/u)
        if asciirr[k] == "0":
            c = int(round(255/lent * y, 0))
        if asciirr[k] == "1":
            c = int(round(255/lent * (lent - y), 0))
        if asciirr[k] == " ":
            c = 255
        c = (c,c,c)
        print(x, y)
        im.putpixel((x, y), c)


im.show()
namea = [random.choice('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890') for _ in range(10)]
name = ""
for i in range(len(namea)):
    name += namea[i]
im.save("../../tests/" + "name" + '.png')
