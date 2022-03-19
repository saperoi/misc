p = []
for a in range(9):
	a += 1
	for b in range(9):
		b += 1
		if a == b:
			continue
		else:
			c = -a - b + 15
			d = -2*a - b + 20
			e = 5
			f = 2*a + b - 10
			g = a + b - 5
			h = 10 - b
			i = 10 - a
			"""
			print(str(a))
			print(str(b))
			print(str(c))
			print(str(d))
			print(str(e))
			print(str(f))
			print(str(g))
			print(str(h))
			print(str(i))
			print(str(a) + str(b) + str(c))
			print(str(d) + str(e) + str(f))
			print(str(g) + str(h) + str(i))
			print()
			"""
			nums = [a, b, c, d, e, f, g, h, i]
			flag = False
			for m in range(len(nums)):
				if nums[m] < 1:
					flag = True
				elif flag == True:
					continue
				else:
					for n in range(len(nums)):
						if m == n:
							continue
						elif flag == True:
							continue
						elif nums[m] == nums[n]:
							flag = True
			if flag == False:
				p.append(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i))

def chunk_str(str, chunk_size):
	return [str[i:i+chunk_size] for i in range(0, len(str), chunk_size)]

for i in range(len(p)):
	r = p[i]
	r = chunk_str(r, 3)
	for i in range(len(r)):
		print(r[i])
	print()
