def save(num): 
	f = open("fizzbuzz.txt", "a")
	f.write('\n' + str(num))
	f.close()

i = 0

while(True):
	r = ""
	if i % 3 == 0:
		r += "Fizz"
	if i % 5 == 0:
		r += "Buzz"
	if r == "":
		r += str(i)
	print(r)
	save(r)
	i += 1
