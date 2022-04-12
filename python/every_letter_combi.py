import random

abl = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def save(txt: str):
	namea = [random.choice('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890') for _ in range(10)]
	name = ""
	for i in range(len(namea)):
		name += namea[i]
	print(name)
	f = open(name + ".txt", "a")
	f.write(txt)
	f.close()

arr = []
for _a in range(len(abl)):
    for _b in range(len(abl)):
        for _c in range(len(abl)):
            for _d in range(len(abl)):
                for _e in range(len(abl)):
                    aa = abl[_a] +  abl[_b] + abl[_c] + abl[_d] + abl[_e]
                    print(aa)
                    arr.append(aa)
str = ""
for _ in range(len(arr)):
    str += arr[_]
    str += "\n"
save(str)

