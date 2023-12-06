def v_calc(c):
    r,g,b = (int(c[:2], 16), int(c[2:][:2], 16), int(c[-2:], 16))
    v = max(r/255, g/255, b/255)
    return v

def rgb2hex(c):
    r, g, b = c
    return '{:02x}{:02x}{:02x}'.format(r, g, b)
def hex2rgb(c):
    return tuple(int(c[i:i+2], 16)  for i in (0, 2, 4))

import random
palette = sorted([rgb2hex((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) for _ in range(16)], key=v_calc)
vs = [0] + [v_calc(c) for c in palette][:-1]
print(vs)

from PIL import Image
ftp = Image.open("src_files/bomb.png").convert(mode="RGB")

size = ftp.size
for x in range(size[0]):
    for y in range(size[1]):
        c = ftp.getpixel((x, y))
        for p in palette:
            if v_calc(rgb2hex(c)) >= vs[palette.index(p)]:
                ftp.putpixel((x,y), hex2rgb(p))
ftp.save("src_files/bomb_o.png", format="PNG")