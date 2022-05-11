from PIL import Image
import os

imgs = os.listdir("./tests")

try:
    imgs.remove("dec_cumyacu.txt")
except:
    pass

d = open("./tests/dec_cumyacu.txt", "a")

for f in range(len(imgs)):
    im = Image.open("./tests/" + imgs[f]) # Can be many different formats.
    pix = im.load()
    width, height = im.size

    binn = ""
    for j in range(height):
        for i in range(width):
            if pix[i, j] == (0, 0, 0):
                binn += "0"
            if pix[i, j] == (255, 255, 255):
                binn += "1"
    
    if (width < 100):
        if width < 10:
            last = "0" + str(width)
        else:
            last = str(width)
        binn = str(int(binn, 2)) + last
    else:
        raise ValueError("Width above 2 digits")
    d.write(binn + "\n\n")
d.close()
