num = 2
low = 2

def save(num): 
	f = open("prime.txt", "a")
	f.write('\n' + str(num))
	f.close()

def calculate(num):
	flag = False
	for i in range(2, 1+num//2):
		if (num % i) == 0:
			flag = True
			break
	
	if flag == False:
		print(num)
		save(num)

while low <= num:
	calculate(num)
	num += 1
