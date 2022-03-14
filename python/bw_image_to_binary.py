from PIL import Image
import os
import codecs

def letterify(bin):
    res = ""
    n = 4
    bin = [bin[i:i+n] for i in range(0, len(bin), n)]
    for i in range(len(bin)):
        if bin[i] == "0000":
            res += "0"
        if bin[i] == "0001":
            res += "1"
        if bin[i] == "0010":
            res += "2"
        if bin[i] == "0011":
            res += "3"
        if bin[i] == "0100":
            res += "4"
        if bin[i] == "0101":
            res += "5"
        if bin[i] == "0110":
            res += "6"
        if bin[i] == "0111":
            res += "7"
        if bin[i] == "1000":
            res += "8"
        if bin[i] == "1001":
            res += "9"
        if bin[i] == "1010":
            res += "A"
        if bin[i] == "1011":
            res += "B"
        if bin[i] == "1100":
            res += "C"
        if bin[i] == "1101":
            res += "D"
        if bin[i] == "1110":
            res += "E"
        if bin[i] == "1111":
            res += "F"
    return res

imgs = os.listdir("./tests")
try:
    imgs.remove("10x")
except:
    exceptingLOL = 1 + 1

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
        s = letterify(bins[p])
        s = int(s, 16) + 32
        print(s)
        s = chr(s)
        print(s)
        try:
            a.write(s)
        except:
            a.write("?")

    b.write("\n\n")
    a.write("\n\n")
b.close()
a.close()