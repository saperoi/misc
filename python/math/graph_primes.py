import numpy as np
from scipy import interpolate
import matplotlib.pyplot as pl

def calculate(num):
    factor = False
    for i in range(2, 1+num//2):
        if (num % i) == 0:
            factor = True
            break
    if factor == False:
        return True
    else:
        return False

j = 10
u = 1001

pl.rcParams['axes.xmargin'] = 0
pl.rcParams['axes.ymargin'] = 0

g = pl.figure()
g.set_size_inches(j, j, forward=True)


xg1 = [0, 1]
yg1 = [0, 0]

for n in range(2, u):
    xg1.append(n)
    if calculate(n) == True:
        yg1.append(yg1[-1] + 1)
    else:
        yg1.append(yg1[-1])
    

x2g1 = np.linspace(xg1[0], xg1[-1], 100)
y2g1 = interpolate.pchip_interpolate(xg1, yg1, x2g1)

pl.plot(x2g1, y2g1)

pl.title("Amount of primes")
pl.xlabel("n")
pl.ylabel("#p")

pl.show()
g.savefig('tests/primes.png')
pl.close(g)