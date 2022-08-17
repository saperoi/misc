from PIL import Image

l = []

for r in range(256):
    for g in range(256):
        for b in range(256):
            if (round(0.0722*b + 0.7152*g + 0.2126*r, 3) == 116.769):
                l.append((r, g, b))
                print((r,g,b))

print(l)

k = 100*len(l)
im = Image.new(mode="RGB", size=(k, k))

for j in range(len(l)):
    print(l[j])
    for x in range(0, k):
        for y in range(100*j+1, 100*(1+j)):
            im.putpixel((x, y), l[j])

im.show()

import random

chars = [random.choice('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890') for _ in range(10)]
name = ""
for i in range(len(chars)):
    name += chars[i]

im.save("tests/" + name + ".png", format="png")