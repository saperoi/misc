import json
doc = open('list.json', 'r')
yassy = json.loads(doc.read())
doc.close()
keys = yassy.keys()
res = open('smashes.txt', 'wb')

for id in keys:
    print(yassy[id]['name'] + ", smash or pass?")
    sop = input()
    out = ""
    if sop.lower() == "smash":
        out = yassy[id]['name'] + ", ID: " + str(id) + ", Image URL: " + yassy[id]['name']
        res.write(out)