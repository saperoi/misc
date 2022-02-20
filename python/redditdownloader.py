import os
import requests
import json

postURLS = ["https://redd.it/jreblp", "https://redd.it/jrebu2", "https://redd.it/js2dwu", "https://redd.it/jt80gq", "https://redd.it/jtyd52", "https://redd.it/jvoo2e", "https://redd.it/jwwehp", "https://redd.it/jy5qu2", "https://redd.it/jzzb9r", "https://redd.it/k1vxg2", "https://redd.it/k36e5h", "https://redd.it/k4f94k", "https://redd.it/k50gis", "https://redd.it/k6en1j", "https://redd.it/k73uuy", "https://redd.it/k7pv9q", "https://redd.it/k8aop6", "https://redd.it/k8tgx1", "https://redd.it/kaaxnx", "https://redd.it/kblaoo", "https://redd.it/ke2ntv", "https://redd.it/kgnr01", "https://redd.it/khabtm", "https://redd.it/kin7an", "https://redd.it/kjvtdq", "https://redd.it/km5ox0", "https://redd.it/knjviz", "https://redd.it/ko7qjv", "https://redd.it/kpz3p1", "https://redd.it/ks8w9p", "https://redd.it/ku7s8f", "https://redd.it/kw9fbp", "https://redd.it/kz1l5f", "https://redd.it/l0zttz", "https://redd.it/l34l70", "https://redd.it/l6qxpc", "https://redd.it/lc1kca", "https://redd.it/leh8xy", "https://redd.it/li3xpv", "https://redd.it/livqas", "https://redd.it/lmh0sd", "https://redd.it/lom6eu", "https://redd.it/lss7yy", "https://redd.it/lwit6i", "https://redd.it/lzjjhm", "https://redd.it/m2if6q", "https://redd.it/m5cww3", "https://redd.it/m92e6d", "https://redd.it/mdfrgz", "https://redd.it/mguwp8", "https://redd.it/mkaxql", "https://redd.it/mojies", "https://redd.it/mshsnf", "https://redd.it/mxfnr9", "https://redd.it/n2ziel", "https://redd.it/n7cs9f", "https://redd.it/ncrbuu", "https://redd.it/niaypm", "https://redd.it/nnef00", "https://redd.it/nshz2p", "https://redd.it/nypvta", "https://redd.it/o3fmkx", "https://redd.it/o8tcjd", "https://redd.it/odfdod", "https://redd.it/oj9khn", "https://redd.it/oql5aa", "https://redd.it/ov3pjw", "https://redd.it/p452eb", "https://redd.it/p8lrxd", "https://redd.it/pdrfir", "https://redd.it/pm2z3d", "https://redd.it/pvlzdh", "https://redd.it/q52eco", "https://redd.it/qhezsc", "https://redd.it/qok423", "https://redd.it/qxbn61", "https://redd.it/qyrdkz", "https://redd.it/r0kiq1", "https://redd.it/r2j64k", "https://redd.it/ra0gzr", "https://redd.it/riarcz", "https://redd.it/s09b86", "https://redd.it/saq0xt"]
HEADERS = {"user-agent": "win64:img-scraper:/u/saperoi"}

def getImg(url: str):
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
    
    try:
        if yassy[0]['data']['children'][0]['data']['is_gallery'] == True:
            keys = yassy[0]['data']['children'][0]['data']['media_metadata'].keys()
            keys = str(keys)
            keys = keys.replace("dict_keys", "")
            keys = keys.replace("(", "")
            keys = keys.replace(")", "")
            keys = keys.replace("[", "")
            keys = keys.replace("]", "")
            keys = keys.replace("'", "")
            keys = keys.replace(" ", "")
            keys = keys.replace("Prolangs ", "")
            keys = keys.split(",")
            for i in range(len(keys)):
                name = yassy[0]['data']['children'][0]['data']['title'] + " #" + str(i+1)
                url = "https://i.redd.it/" + keys[i-1] + ".png"
                dlIMG(url, name)
    except:
        url = yassy[0]['data']['children'][0]['data']['url']
        name = yassy[0]['data']['children'][0]['data']['title']
        dlIMG(url, name)

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
    name = name.replace("amp;", "")
    #print(name)
    img = open('./redddit/' + str(name) + '.png', 'wb')
    img.write(r.content)
    img.close()

for link in postURLS:
    link = link.replace("redd.it", "www.reddit.com/comments")
    getImg(link)

input("Press any key to exit")
