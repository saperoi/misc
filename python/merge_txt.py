import os
import requests

betalink = "https://cdn.discordapp.com/attachments/947100010959470595/955565508533555220/jewdle_alpha.txt"
gammalink = "https://cdn.discordapp.com/attachments/947100010959470595/955565318971994162/jewdle_gamma.txt"

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

epsilon = open("tests/jewdle_gamma.txt", "a")
for i in range(len(betaf)):
    if betaf[i] not in gammaf:
        epsilon.write(betaf[i])
        epsilon.write(gammaf[i])
    else:
        epsilon.write(gammaf[i])

os.remove("g.txt")
os.remove("b.txt")