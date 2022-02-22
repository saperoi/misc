import os
import requests
import json

id = 1
namepi = "https://pogoapi.net/api/v1/pokemon_names.json"

r = requests.get(namepi)
doc = open('pkmn.json', 'wb')
doc.write(r.content)
doc.close()
yassyrn = open('pkmn.json')
yassyn = json.loads(yassyrn.read())
yassyrn.close()
os.remove('pkmn.json')

res = open("list.json", "a")
res.write("{\n")

res2 = open("list.txt", "a")

while id <= 905:
	name = ""
	try:
		name = yassyn[str(id)]["name"]
	except:
		name = "???"
	link = "https://serebii.net/art/th/" + str(id) + ".png"
	if len(str(id)) == 1:
		id = "00" + str(id)
	if len(str(id)) == 2:
		id = "0" + str(id)
	res.write("\t\"" + str(int(id)) + "\": {\n")
	res.write("\t\t\"name\": \"" + name  + "\",\n")
	res.write("\t\t\"id\": \"" + str(id) + "\",\n")
	res.write("\t\t\"url\": \"" + link + "\"\n")
	if str(id) == "905":
		res.write("\t}\n")
	else:
		res.write("\t},\n")
	res2.write(name + ", " + str(id) + ", " + link + "\n")
	id = int(id) + 1


res.write("}")
