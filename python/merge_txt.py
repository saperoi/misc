import os
import requests

betalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/giant.txt"
gammalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/giant256.txt"

r = requests.get(betalink)
betaf = open("b.txt", "wb")
betaf.write(r.content)
betaf.close()
betaf = open("b.txt", "r").readlines()

r = requests.get(gammalink)
gammaf = open("g.txt", "wb")
gammaf.write(r.content)
gammaf.close()
gammaf = open("g.txt", "r").readlines()

epsilon = open("src_files/dict/256combo.txt", "a")
for i in range(len(betaf)):
    epsilon.write(betaf[i])
    epsilon.write(gammaf[i])

os.remove("g.txt")
os.remove("b.txt")