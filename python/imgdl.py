import os
import requests
import json
import random

link = ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Large_World_Map_bright.jpg"]


def getImg(url: str, ext:str):
    r = requests.get(url)
    doc = open(r(), 'wb')
    doc.write(r.content)
    doc.close()

def r():
    chars = [random.choice('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890') for _ in range(10)]
    name = ""
    for i in range(len(chars)):
        name += chars[i]
    return name

for i in range(len(a)):
    ext = link[i].split('.')
    ext = '.' + ext[-1]
    getImg(link[i], ext)

input("Press any key to exit")
