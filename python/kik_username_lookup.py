import json
import os
import requests

def getJSON(name):
    r = requests.get('https://ws2.kik.com/user/' + name)
    doc = open('req.json', 'wb')
    doc.write(r.content)
    doc.close()
    try:
        yassyrn = open('req.json', 'rb')
        yassyn = json.loads(yassyrn.read())
        yassyrn.close()
        os.remove('req.json')
    except:
        f = open("errored.txt", "a", encoding="utf-8")
        f.write(name + "\n")
        f.close()
        errr = '{"firstName":"ERROR","lastName":"ERROR","displayPicLastModified":"ERROR","displayPic":"ERROR"}'
        yassyn = json.loads(errr)
        
    return yassyn

fnames = open("usernames.txt", "r")
fname = fnames.readlines()
fnames.close()
names = []
for _ in range(len(fname)):
    names.append(fname[_].replace("\n", ""))



for i in range(len(names)):
    print(names[i])
    j = getJSON(names[i])
    print(j)
    f = open("res.txt", "a", encoding="utf-8")
    f.write('Username: ' + str(names[i]))
    print(names[i])
    f.write('\nFirst Name: ' + str(j['firstName']))
    f.write('\nLast Name: ' + str(j['lastName']))
    try:
        f.write('\nPFP Link: ' + str(j['displayPic']))
    except:
        f.write('\nPFP Link: ERROR')
    try:
        f.write('\nLast PFP Update: ' + str(j['displayPicLastModified']))
    except:
        f.write('\nLast PFP Update: ERROR')
    f.write('\n-------\n')
    f.close()
