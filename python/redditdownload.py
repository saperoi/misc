import os
import requests
import json

postURLS = ["LITERALLY EVERY LINK IN THE SHEET I COPIED AND CTRL H'd FOR THE APOSTAPHE AND COMMAS"]
HEADERS = {"user-agent": "win64:img-scraper:/u/saperoi"}

def getImgLink(url):
	#x[0].data.children[0].data.url
	url = url + '.json'
	r = requests.get(url, headers=HEADERS)
	doc = open('page.json', 'wb')
	doc.write(r.content)
	doc.close()
	yassyr = open('page.json')
	yassy = json.loads(yassyr.read())
	yassyr.close()
	os.remove('page.json')
	return yassy[0]['data']['children'][0]['data']['url'], yassy[0]['data']['children'][0]['data']['title']

def dlIMG(url, name):
	r = requests.get(url, headers=HEADERS)
	name = name.replace(":", "")
	name = name.replace("?", "")
	name = name.replace("(", "")
	name = name.replace(")", "")
	name = name.replace("'", "")
	name = name.replace("!", "")
	name = name.replace(".", "")
	name = name.replace(",", "")
	name = name.replace('"', "")
	print(name)
	img = open('./redddit/' + str(name) + '.png', 'wb')
	img.write(r.content)
	img.close()

for link in postURLS:
	imgLink, name = getImgLink(link)
	print(imgLink)
	dlIMG(imgLink, name)
