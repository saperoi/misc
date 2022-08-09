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


s = open('ss.txt', 'w')
s.write('')
s.close()
s = open('ss.txt', 'a')

f = open('color.txt')
sl = f.read().splitlines()
f.close()

for i in range(len(sl)):
    sl[i] = sl[i][-6:] + " " + sl[i]

sl.sort()

for j in range(len(sl)):
    sl[j] = sl[j][7:]

for k in sl:
    s.write(k + "\n")

s.close()




n = open('ns.txt', 'w')
n.write('')
n.close()
n = open('ns.txt', 'a')

f = open('color.txt')
nl = f.read().splitlines()
f.close()

nl.sort()

for k in nl:
    n.write(k + "\n")

n.close()




b = open('base.txt')
bl = b.read().splitlines()
b.close()




r = open('color.html', 'w')
r.write('')
r.close()
r = open('color.html', 'a')

f = open('color.txt')
rl = f.read().splitlines()
f.close()

for _ in bl:
    r.write(_ + '\n')

for k in rl:
    k = k.replace("&", "&amp;")
    p = k[-6:]
    if(isLight(p)):
        r.write('    <p style="background-color: #' + p + '; color: black;"> &emsp;&emsp; ' + k[:-7] + ' &emsp;&emsp; #' + p + ' </p>\n')
    else:
        r.write('    <p style="background-color: #' + p + ';"> &emsp;&emsp; ' + k[:-7] + ' &emsp;&emsp; #' + p + ' </p>\n')
r.write('</body>')
r.close()




r = open('colorhex.html', 'w')
r.write('')
r.close()
r = open('colorhex.html', 'a')

f = open('ss.txt')
ssl = f.read().splitlines()
f.close()

for _ in bl:
    r.write(_ + '\n')

for k in ssl:
    k = k.replace("&", "&amp;")
    p = k[-6:]
    if(isLight(p)):
        r.write('    <p style="background-color: #' + p + '; color: black;"> &emsp;&emsp; ' + k[:-7] + ' &emsp;&emsp; #' + p + ' </p>\n')
    else:
        r.write('    <p style="background-color: #' + p + ';"> &emsp;&emsp; ' + k[:-7] + ' &emsp;&emsp; #' + p + ' </p>\n')
r.write('</body>')

r.close()




r = open('colorname.html', 'w')
r.write('')
r.close()
r = open('colorname.html', 'a')

f = open('ns.txt')
nsl = f.read().splitlines()
f.close()

for _ in bl:
    r.write(_ + '\n')

for k in nsl:
    k = k.replace("&", "&amp;")
    p = k[-6:]
    if(isLight(p)):
        r.write('    <p style="background-color: #' + p + '; color: black;"> &emsp;&emsp; ' + k[:-7] + ' &emsp;&emsp; #' + p + ' </p>\n')
    else:
        r.write('    <p style="background-color: #' + p + ';"> &emsp;&emsp; ' + k[:-7] + ' &emsp;&emsp; #' + p + ' </p>\n')

r.write('</body>')

r.close()
