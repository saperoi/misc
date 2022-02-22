import math
import random

global ablist
abl = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def save(txt: str):
	name = str([random.choice('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890') for _ in range(10)])
	print(name)
	f = open(name + ".txt", "w")
	f.write(txt)
	f.close()

def ab(start: int = 1, end: int = 26, style: str = 'h',):
	resa = []
	rest = ''

	for i in range(start, end + 1):
		colm = ''
		pos = i % 26
		if pos == 0:
			pos = 26
		xtra = math.floor((i-1)/26)
		while xtra > 26:
			colm += 'Z'
			xtra -= 26	
		if 26 >= xtra > 0:
			colm += abl[xtra-1]
		colm += abl[pos-1]
		#print(colm)
		resa.append(colm)

	if style == "vertically" or 'vert' or 'v':
		for i in range(len(resa)):
			rest += str(resa[i]) + '\n'
			print(rest)
	if style == "horizontally" or 'horiz' or 'h':
		for i in range(len(resa)):
			rest += str(resa[i]) + '\t'
			print(rest)
	
	save(rest)

def num(style: str = 'v', start: int = 1, end: int = 10):
	resa = []
	rest = ''
	
	for x in range(start, end+1):
		resa.append(str(x))
		#print(x)

	if style == "vertically" or 'vert' or 'v':
		for i in range(len(resa)):
			rest += str(resa[i]) + '\n'
			print(rest)
	if style == "horizontally" or 'horiz' or 'h':
		for i in range(len(resa)):
			rest += str(resa[i]) + '\t'
			print(rest)
		
	save(rest)

#ab("v", 1, 20)
#num("h", 30, 60)
#ab("h", 60*10, 70*9)
ab(style = "h")