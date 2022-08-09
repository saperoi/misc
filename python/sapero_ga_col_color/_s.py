f = open('color.txt')
r = open('sort.txt', 'w')
r.write('')
r.close()
r = open('sort.txt', 'a')

fl = f.read().splitlines()
f.close()

for i in range(len(fl)):
    fl[i] = fl[i][-6:] + " " + fl[i]

fl.sort()

for j in range(len(fl)):
    fl[j] = fl[j][7:]

for k in fl:
    r.write(k + "\n")