import numpy as np
from scipy import interpolate
import matplotlib.pyplot as pl

pl.rcParams['axes.xmargin'] = 0
pl.rcParams['axes.ymargin'] = 0

g1 = pl.figure()
g1.set_size_inches(8.3, 11.7, forward=True)

xg1=[0,1,2,3,4]
yg1=[17,12,4,3,1]

"""
x2g1 = np.array(x)
y2g1 = np.array(y)

"""
x2g1 = np.linspace(xg1[0], xg1[-1], 100)
y2g1 = interpolate.pchip_interpolate(xg1, yg1, x2g1)

pl.vlines(1.4545454545454546, 0, 7.912076903812442, color='red', linestyle='dotted')
pl.hlines(7.912076903812442, 0, 1.4545454545454546, color='red', linestyle='dotted')

pl.text(1.5, 8, r'$T_{1/2} = 1.45$', fontsize=14)

pl.plot(x2g1, y2g1)
pl.plot(xg1, yg1, "o")

_ = 0
__ = [0]
while _ < max(yg1):
    _ += 2
    __.append(_)

pl.yticks(__ + yg1)
pl.xticks(xg1)

pl.title("Groep 1 - 17 Munten")
pl.xlabel("Aantal worpen")
pl.ylabel("Aantal munten")

pl.show()
g1.savefig('tests/1.png')
pl.close(g1)


# ----------------------------------------------------------

g2 = pl.figure()
g2.set_size_inches(8.3, 11.7, forward=True)

xg2=[0,1,2,3,4,5]
yg2=[44,26,14,6,4,0]

"""
x2g2 = np.array(x)
y2g2 = np.array(y)

"""
x2g2 = np.linspace(xg2[0], xg2[-1], 100)
y2g2 = interpolate.pchip_interpolate(xg2, yg2, x2g2)

pl.vlines(1.2121212121212122, 0, 23.0534435261708, color='red', linestyle='dotted')
pl.hlines(23.0534435261708, 0, 1.2121212121212122, color='red', linestyle='dotted')
pl.text(1.25, 23.5, r'$T_{1/2} = 1.2$', fontsize=14)
pl.plot(x2g2, y2g2)
pl.plot(xg2, yg2, "o")

_ = 0
__ = [0]
while _ < max(yg2):
    _ += 5
    __.append(_)

pl.yticks(__ + yg2)
pl.xticks(xg2)

pl.title("Groep 2 - 44 Munten")
pl.xlabel("Aantal worpen")
pl.ylabel("Aantal munten")

pl.show()
g2.savefig('tests/2.png')
pl.close(g2)

# ----------------------------------------------------------

g3 = pl.figure()
g3.set_size_inches(8.3, 11.7, forward=True)

xg3=[0,1,2,3,4,5,6,7,8]
yg3=[166,83,46,29,14,5,3,2,0]

"""
x2g3 = np.array(x)
y2g3 = np.array(y)

"""
x2g3 = np.linspace(xg3[0], xg3[-1], 100)
y2g3 = interpolate.pchip_interpolate(xg3, yg3, x2g3)

pl.vlines(1, 0, 83, color='red', linestyle='dotted')
pl.hlines(83, 0, 1, color='red', linestyle='dotted')
pl.text(1.1, 83.5, r'$T_{1/2} = 1$', fontsize=14)

pl.plot(x2g3, y2g3)
pl.plot(xg3, yg3, "o")

_ = 0
__ = [0]
while _ < max(yg3):
    _ += 20
    __.append(_)

pl.yticks(__ + yg3)
pl.xticks(xg3)

pl.title("Groep 3 - 166 Munten")
pl.xlabel("Aantal worpen")
pl.ylabel("Aantal munten")

pl.show()
g3.savefig('tests/3.png')
pl.close(g3)
