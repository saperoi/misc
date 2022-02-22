import json
import requests
import os
from colorit import color_back
from PIL import Image

doc = open('list.json', 'r')
yassy = json.loads(doc.read())
doc.close()
keys = yassy.keys()
res = open('smashes.txt', 'wb')

for id in keys:
    print(yassy[id]['name'] + ", smash or pass?")
    r = requests.get(yassy[id]['url'])
    doc = open(str(id) + '.png', 'wb')
    doc.write(r.content)
    doc.close()
    image = Image.open(str(id) + '.png')
    image.show()
    sop = input()
    out = ""
    if sop.lower() == "smash":
        out = yassy[id]['name'] + ", ID: " + str(id) + ", Image URL: " + yassy[id]['name']
        res.write(out)
    image.close()
    os.remove(str(id) + '.png')