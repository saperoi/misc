import random as r
from PIL import Image
import time
start = time.time()
s = 1000
sprinkles = 24000
skipped = 0

m = [[None for _ in range(s+2)] for _ in range(s+2)] #matrix with all the things
m2 = [[None for _ in range(s+2)] for _ in range(s+2)] #just for overlap check
m4 = [[None for _ in range(s+2)] for _ in range(s+2)] #just for overlap check
m3 = [[False for _ in range(s+2)] for _ in range(s+2)]

w = (255,255,255)
b = (0,0,0)

sprinkleColorMode = "randmono" #multi, mono, defined, randmono, black
if sprinkleColorMode == "defined":
    definedSeed = "hash" #hash, order

def hsv_to_rgb(h):
    if 0 <= h < 60:
        return 255, round((1 - abs((h / 60) % 2 - 1)) * 255), 0
    elif 60 <= h < 120:
        return round((1 - abs((h / 60) % 2 - 1)) * 255), 255, 0
    elif 120 <= h < 180:
        return 0, 255, round((1 - abs((h / 60) % 2 - 1)) * 255)
    elif 180 <= h < 240:
        return 0, round((1 - abs((h / 60) % 2 - 1)) * 255), 255
    elif 240 <= h < 300:
        return round((1 - abs((h / 60) % 2 - 1)) * 255), 0, 255
    else:
        return 255, 0, round((1 - abs((h / 60) % 2 - 1)) * 255)

tiny = [
[[b,b,b],[b,w,b],[b,b,b]],
[[b,b,b],[w,w,w],[b,b,b]],
[[b,w,b],[b,w,b],[b,w,b]],
[[w,w,b],[w,b,w],[b,w,w]],
[[b,w,w],[w,b,w],[w,w,b]],
[[b,w,b],[w,w,w],[b,w,b]],
[[b,w,b],[b,w,b],[b,b,b]],
[[b,b,b],[w,w,b],[b,b,b]],
[[b,b,b],[b,w,b],[b,w,b]],
[[b,b,b],[b,w,w],[b,b,b]],
[[b,w,b],[w,b,w],[b,w,b]],
[[w,b,w],[b,w,b],[w,b,w]],
[[b,b,b],[b,b,b],[b,b,b]],
[[w,b,w],[b,b,b],[w,b,w]],
[[b,w,w],[b,w,w],[b,b,b]],
[[b,b,b],[b,w,w],[b,w,w]],
[[b,b,b],[w,w,b],[w,w,b]],
[[w,w,b],[w,w,b],[b,b,b]],
]

r.shuffle(tiny)

for i in range(sprinkles):
    t = r.randint(0,len(tiny)-1)
    x,y = (r.randint(0,s-1),r.randint(0,s-1))
    if any(_ is not None for _ in [m[y][x], m[y][x+1], m[y][x+2], m[y+1][x], m[y+1][x+1], m[y+1][x+2], m[y+2][x], m[y+2][x+1], m[y+2][x+2]]):
        if any(_ is not False for _ in [m3[y][x], m3[y][x+1], m3[y][x+2], m3[y+1][x], m3[y+1][x+1], m3[y+1][x+2], m3[y+2][x], m3[y+2][x+1], m3[y+2][x+2]]):
            skipped += 1
            continue
        else:
            z = set([_ for _ in [m4[y][x], m4[y][x+1], m4[y][x+2], m4[y+1][x], m4[y+1][x+1], m4[y+1][x+2], m4[y+2][x], m4[y+2][x+1], m4[y+2][x+2]] if _ != None])
            if len(z) > 1:
                skipped += 1
                continue
            x2,y2 = list(z)[0]
            m3[y2][x2], m3[y2][x2+1], m3[y2][x2+2], m3[y2+1][x2], m3[y2+1][x2+1], m3[y2+1][x2+2], m3[y2+2][x2], m3[y2+2][x2+1], m3[y2+2][x2+2] = (True,)*9
            m3[y][x], m3[y][x+1], m3[y][x+2], m3[y+1][x], m3[y+1][x+1], m3[y+1][x+2], m3[y+2][x], m3[y+2][x+1], m3[y+2][x+2] = (True,)*9
    m[y][x], m[y][x+1], m[y][x+2], m[y+1][x], m[y+1][x+1], m[y+1][x+2], m[y+2][x], m[y+2][x+1], m[y+2][x+2], m2[y][x] = (t,)*10
    m4[y][x], m4[y][x+1], m4[y][x+2], m4[y+1][x], m4[y+1][x+1], m4[y+1][x+2], m4[y+2][x], m4[y+2][x+1], m4[y+2][x+2] = ((x,y),)*9

img = Image.new('RGB', (s+2,s+2), color = w)

for y in range(s):
    for x in range(s):
        if m2[y][x] != None:
            u = m2[y][x]
            c = tiny[u]
            if sprinkleColorMode == "multi":
                cwb = lambda x: hsv_to_rgb(r.randint(0,360)) if x == b else w
            elif sprinkleColorMode == "mono":
                color = hsv_to_rgb(round(360/len(tiny)*u))
                cwb = lambda x: color if x == b else w
            elif sprinkleColorMode == "randmono":
                color = r.randint(0x0, 0xffffff-1)
                cwb = lambda x: color if x == b else w
            elif sprinkleColorMode == "defined":
                if definedSeed == "hash":
                    import hashlib
                    seeder = int(hashlib.sha256(str(tiny[u]).encode('utf-8')).hexdigest(), 16)
                elif definedSeed == "order":
                    import hashlib
                    seeder = u
                cwb = lambda x: [r.seed(seeder), r.randint(0x0, 0xffffff) if x == b else w][1]
            elif sprinkleColorMode == "black":
                cwb = lambda x: x
            if m[y][x] == u:
                img.putpixel((x,y), cwb(c[0][0]))
            if m[y][x+1] == u:
                img.putpixel((x+1,y), cwb(c[0][1]))
            if m[y][x+2] == u:
                img.putpixel((x+2,y), cwb(c[0][2]))
            if m[y+1][x] == u:
                img.putpixel((x,y+1), cwb(c[1][0]))
            if m[y+1][x+1] == u:
                img.putpixel((x+1,y+1), cwb(c[1][1]))
            if m[y+1][x+2] == u:
                img.putpixel((x+2,y+1), cwb(c[1][2]))
            if m[y+2][x] == u:
                img.putpixel((x,y+2), cwb(c[2][0]))
            if m[y+2][x+1] == u:
                img.putpixel((x+1,y+2), cwb(c[2][1]))
            if m[y+2][x+2] == u:
                img.putpixel((x+2,y+2), cwb(c[2][2]))

end = time.time()
print(end-start, skipped)
img.show()
img.save(f"{"".join([r.choice(list('abcdefghijklmnopqrstuvwxyz')) for _ in range(10)])}.png")