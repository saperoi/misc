a = ["redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted", "redacted"]
f = open("links.txt", "w")
i = 0
while i <= len(a):
	print(i)
	print(a[i])
	url = "https://docs.google.com/spreadsheets/d/" + a[i] + "/edit?usp=sharing \n"
	print(url)
	f.write(url)
	i += 1
