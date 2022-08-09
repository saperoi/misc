f = open('color.txt')
r = open('sort.txt', 'w')
r.write('')
r.close()
r = open('sort.txt', 'a')

fl = f.read().splitlines()
f.close()

fl.sort()

for k in fl:
    r.write(k + "\n")