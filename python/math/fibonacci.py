f1 = 1
f2 = 0
num = 1
low = 1

def save(num): 
	f = open("fibonacci.txt", "a")
	f.write('\n' + str(num))
	f.close()

while low <= num:
	num = f1 + f2
	print(num)
	save(num)
	f1 = f2
	f2 = num
