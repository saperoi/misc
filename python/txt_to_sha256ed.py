from hashlib import sha256
import os
import requests

alphalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/giant.txt"
r = requests.get(alphalink)
res = open("res.txt", "a")
alpha = open("w.txt", "wb")
alpha.write(r.content)
alpha.close()
alpha = open("w.txt", "r")
data = alpha.readlines()
for i in range(len(data)):
    hashed = data[i].replace("\n", "")
    hashed = sha256(hashed.encode('utf-8')).hexdigest()
    res.write(hashed + "\n")
alpha.close()
os.remove("w.txt")