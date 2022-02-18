f1 = 1
f2 = 0
f3 = 0
num = 1
low = 1

def save(num): 
	f = open("tribonacci.txt", "a")
	f.write('\n' + str(num))
	f.close()

while low <= num:
	num = f1 + f2 + f3
	print(num)
	save(num)
	f1 = f2
	f2 = f3
	f3 = num
