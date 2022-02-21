import random
import os

resd = open('plates.txt', 'a+')
while True:
	start = [random.choice('111111122228TMTM') for _ in range(1)]
	lette = [random.choice('AZERTYUIOPQSDFGHJKLMWXCVBN') for _ in range(3)]
	numdo = [random.choice('0123456789') for _ in range(3)]
	res = start[0] + "-" + lette[0] + lette[1] + lette[2] + "-" + numdo[0] + numdo[1] + numdo[2]
	print(res)
	resd.write(res + "\n")
