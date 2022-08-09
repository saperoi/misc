import math

def isLight(h):
    rc = h[:2]
    r = int(rc, 16)
    gc = h[-4:][:2]
    g = int(gc, 16)
    bc = h[-2:]
    b = int(bc, 16)

    perc = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    if perc > 180:
        return True
    else:
        return False

b = open('base.txt')
bl = b.read().splitlines()
b.close()

r = open('all.html', 'w')
r.write('')
r.close()
r = open('all.html', 'a')

rl = []

for a in range(256):
    x = hex(a)
    if len(x) == 3:
        x = '0x0' + x[-1:]
    x = x[-2:]
    print(x)
    for b in range(256):
        y = hex(b)
        if len(y) == 3:
            y = '0x0' + y[-1:]
        y = y[-2:]
        for c in range(256):
            z = hex(c)
            if len(z) == 3:
                z = '0x0' + z[-1:]
            z = z[-2:]
            _ = x +  y + z
            rl.append(_)

print('done')

for _ in bl:
    r.write(_ + '\n')
for p in rl:
    if(isLight(p)):
        r.write('    <p style="background-color: #' + p + '; color: black;"> &emsp;&emsp; #' + p + ' </p>\n')
    else:
        r.write('    <p style="background-color: #' + p + ';"> &emsp;&emsp; #' + p + ' </p>\n')
r.write('</body>')
r.close()
