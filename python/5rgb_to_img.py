import base64
import json
from PIL import Image

def hextodec(n):
    n = list(n)
    c = 0
    for i in range(len(n)):
        if n[i] == "a":
            n[i] = 10
        if n[i] == "b":
            n[i] = 11
        if n[i] == "c":
            n[i] = 12
        if n[i] == "d":
            n[i] = 13
        if n[i] == "e":
            n[i] = 14
        if n[i] == "f":
            n[i] = 15
    c += int(n[0]) * 16
    c += int(n[1])
    return c

f = open('../tests/hex.txt')
a = f.readlines()
f.close()
    
hc1 = a[0].replace("#","").replace("\n","").lower()
hc2 = a[1].replace("#","").replace("\n","").lower()
hc3 = a[2].replace("#","").replace("\n","").lower()
hc4 = a[3].replace("#","").replace("\n","").lower()
hc5 = a[4].replace("#","").replace("\n","").lower()
hc1 = (hextodec(hc1[:2]), hextodec(hc1[-4:][:2]), hextodec(hc1[-2:]))
hc2 = (hextodec(hc2[:2]), hextodec(hc2[-4:][:2]), hextodec(hc2[-2:]))
hc3 = (hextodec(hc3[:2]), hextodec(hc3[-4:][:2]), hextodec(hc3[-2:]))
hc4 = (hextodec(hc4[:2]), hextodec(hc4[-4:][:2]), hextodec(hc4[-2:]))
hc5 = (hextodec(hc5[:2]), hextodec(hc5[-4:][:2]), hextodec(hc5[-2:]))
print(hc1)

im = Image.new(mode="RGB", size=(2000, 2000))

for x in range(0, 2000):
    for y1 in range(0, 400):
        im.putpixel((x, y1), hc1)
    for y2 in range(401, 800):
        im.putpixel((x, y2), hc2)
    for y3 in range(801, 1200):
        im.putpixel((x, y3), hc3)
    for y4 in range(1201, 1600):
        im.putpixel((x, y4), hc4)
    for y5 in range(1601, 2000):
        im.putpixel((x, y5), hc5)

im.show()

import random

chars = [random.choice('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890') for _ in range(10)]
name = ""
for i in range(len(chars)):
    name += chars[i]

im.save("../tests/" + name + ".png", format="png")
