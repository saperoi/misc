from PIL import Image
f = Image.open('src_files/notes.png')
name = "notes"
ix,iy= f.size

def rotate(l, n):
    return l[n:] + l[:n]

m = []
for x in range(ix):
    n = []
    for y in range(iy):
        n.append(f.getpixel((x,y)))
    m.append(n)

for _ in range(ix):
    for x in range(ix):
        for y in range(iy):
            print(x, y, m[x][y])
            f.putpixel((x,y), m[x][y])
    m = rotate(m, 1)
    f.save(f"src_files/{name}/{_}.png")
    