num = 1
answer = 0
low = 1

def save(num): 
	f = open("triangular.txt", "a")
	f.write('\n' + str(num))
	f.close()

while low <= num:
	answer = num * (num + 1) // 2
	print(answer)
	save(answer)
	num += 1
