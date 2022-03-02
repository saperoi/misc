from PIL import Image
import os
import binascii

imgs = os.listdir("./tests")
imgs.remove("10x")

try:
    imgs.remove("ascii.txt")
except:
    exceptingLOL = 1 + 1

try:
    imgs.remove("binary.txt")
except:
    exceptingLOL = 1 + 1

b = open("./tests/binary.txt", "a")
a = open("./tests/ascii.txt", "a")

for f in range(len(imgs)):
    im = Image.open("./tests/" + imgs[f]) # Can be many different formats.
    pix = im.load()
    width, height = im.size

    bins = []

    for i in range(width):
        res = ""
        for j in range(height):
            if pix[i,j] == (0, 0, 0):
                res += "0"
            if pix[i,j] == (255, 255, 255):
                res += "1"
        bins.append(res)
    
    for p in range(len(bins)):
        b.write(bins[p] + "\n")
        s = bins[p]
        message = ""
        while s != "":
            i = chr(int(s[:8], 2))
            message = message + i
            s = s[8:]
        a.write(message)

b.write("\n\n")
a.write("\n\n")
b.close()
a.close()