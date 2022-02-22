import base64
from PIL import Image

def splito(url, r):
	url = url[-11:]
	print(url)
	url += r
	c1 = url[:4]
	print(c1)
	c2 = url[-8:][:4]
	print(c2)
	c3 = url[-4:]
	print(c3)
	return c1, c2, c3

def hextodec(n):
	n = n.lower()
	n = list(n)
	c = 0
	for i in range(len(n)):
		if n[i] == "a":
			n[i] = 10
		if n[i] == "b":
			n[i] = 11
		if n[i] == "c":
			n[i] = 12
		if n[i] == "d":
			n[i] = 13
		if n[i] == "e":
			n[i] = 14
		if n[i] == "f":
			n[i] = 15
		c += int(n[i]) * (len(n) - i) * 16
	return c

url = input("Link: ")
r = input("Random character: ")
while r not in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789-_":
	r = input("Not allowed, put other character in. ")
c1, c2, c3 = splito(url, r)
hc1 = str(base64.b16encode(base64.urlsafe_b64decode(c1))).replace("b'", "").replace("'", "")
hc2 = str(base64.b16encode(base64.urlsafe_b64decode(c2))).replace("b'", "").replace("'", "")
hc3 = str(base64.b16encode(base64.urlsafe_b64decode(c3))).replace("b'", "").replace("'", "")
print(hc1, hc2, hc3)
hc1 = (hextodec(hc1[:2]), hextodec(hc1[-4:][:2]), hextodec(hc1[-2:]))
hc2 = (hextodec(hc2[:2]), hextodec(hc2[-4:][:2]), hextodec(hc2[-2:]))
hc3 = (hextodec(hc3[:2]), hextodec(hc3[-4:][:2]), hextodec(hc3[-2:]))

im = Image.new(mode="RGB", size=(1200, 1200))

for x in range(0, 1200):
    for y in range(0, 400):
        im.putpixel((x, y), hc1)
for x in range(0, 1200):
    for y in range(401, 800):
        im.putpixel((x, y), hc2)
for x in range(0, 1200):
    for y in range(801, 1200):
        im.putpixel((x, y), hc3)

im.show()