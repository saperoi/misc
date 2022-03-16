import matplotlib.pyplot as plt
import numpy as np

p = [(4, 4), (4, 5), (4, 6), (5, 6), (5, 5), (6, 5), (6, 7), (6, 6), (7, 5), (7, 6), (7, 8), (7, 7), (8, 6), (8, 9), (8, 7), (9, 6), (9, 10), (9, 8), (10, 11), (10, 9), (10,6), (10, 8), (11, 6), (11, 12), (11, 10)]
x = []
y = []
for i in range(len(p)):
    a, b = p[i]
    x.append(a)
    y.append(b)

plt.scatter(x, y)

"""
n = []
m = []
for j in range(11):
    n.append(j)
    m.append(4 + max(2, (j-5)))
plt.plot(n, m, 'k')

n = []
m = []
for j in range(11):
    n.append(j)
    m.append(j+1)
plt.plot(n, m, 'b')

n = []
m = []
for j in range(11):
    n.append(j)
    m.append(1 - max(0, -j+5) + 6)
plt.plot(n, m, 'g')

n = []
m = []
for j in range(11):
    n.append(j)
    m.append(6)
plt.plot(n, m, 'b')
"""
plt.savefig('tests/wrdle.png')
plt.show()
plt.close
