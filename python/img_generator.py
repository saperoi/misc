"""

Uses pre existing images n shit

"""

import os
import sys
import random
from PIL import Image

PATH = "F:/IcosaNFT"

def NFTCreator(c, g, w, n):
    nft = Image.new("RGBA", (128,128), (0, 0, 0, 255))
    nft.paste(g,(0,0),g)
    nft.paste(c,(0,0),c)
    #nft.paste(w,(0,0),w)
    
    open(PATH + "/nft/" + str(n) + ".png", mode="ab+")
    nft.save(PATH + "/nft/" + str(n) + ".png", format="png")
  
def GenTrait():
    TopTrait()
    BodyTrait()
    ColorTrait()
    BGTrait()
    WearTrait()

def RandomNFT():
    GenTrait()
    name = str(3**bgt * 5**colort * 7**bodyt * 11**topt) #2**weart *
    if os.path.isfile(PATH + "/nft/" + str(name) + ".png"):
        GenNFT = Image.open(PATH + "/nft/" + str(name) + ".png").convert(mode="RGBA")
    else:
        NFTCreator(colorimg, bgimg, wearimg, name)
    traits = topn + ", " + bodyn + ", " + colorn + ", " + bgn # + ", " + wearn
    tf = open("traits.txt", "a+")
    tf.write(traits + "\n")
    tf.close

n = 0
while n < 100000:
    RandomNFT()
    n += 1

def TopTrait():
    global topt
    global topn
    global topimg
    topt = random.randint(0,1)
    if topt == 0:
        topn = "2Top"
    if topt == 1:
        topn = "3Top"

def BodyTrait():
    global bodyt
    global bodyn
    global bodyimg
    bodygen = 3 #random.randint(0,5)
    if bodygen == 3:
        bodyt = 1
        bodyn = "Floating"
    else:
        bodyt = 0
        bodyn = "Attached"

def ColorTrait():
    global colort
    global colorn
    global colorimg
    randomint0 = random.randint(0,23)
    
    if randomint0 == 0:
        colort = 0
        colorn = "White"
    if randomint0 == 1:
        colort = 1
        colorn = "Pink"
    if randomint0 == 2:
        colort = 2
        colorn = "Red"
    if randomint0 == 3:
        colort = 3
        colorn = "Crimson"
    if randomint0 == 4:
        colort = 4
        colorn = "Orange"
    if randomint0 == 5:
        colort = 5
        colorn = "Brown"
    if randomint0 == 6:
        colort = 6
        colorn = "Yellow"
    if randomint0 == 7:
        colort = 7
        colorn = "Light Green"
    if randomint0 == 8:
        colort = 8
        colorn = "Green"
    if randomint0 == 9:
        colort = 9
        colorn = "Dark Green"
    if randomint0 == 10:
        colort = 10
        colorn = "Light Blue"
    if randomint0 == 11:
        colort = 11
        colorn = "Blue"
    if randomint0 == 12:
        colort = 12
        colorn = "Dark Blue"
    if randomint0 == 13:
        colort = 13
        colorn = "Light Purple"
    if randomint0 == 14:
        colort = 14
        colorn = "Purple"
    if randomint0 == 15:
        colort = 15
        colorn = "Dark Purple"
    if randomint0 >= 16:
        randomint1 = random.randint(0,2)
        if randomint1 == 0:
            colort = 16
            colorn = "Black"
        if randomint1 == 1:
            colort = 17
            colorn = "Silver"
        if randomint1 == 2:
            randomint2 = random.randint(0,4)
            if randomint2 == 0:
                colort = 18
                colorn = "Yellow And Purple"
            if randomint2 == 1:
                colort = 19
                colorn = "Blue And Pink"
            if randomint2 == 2:
                colort = 20
                colorn = "Black And Yellow"
            if randomint2 == 3:
                colort = 21
                colorn = "Black And Pink"
            if randomint2 == 4:
                randomint3 = random.randint(0,2)
                if randomint3 == 0:
                    colort = 22
                    colorn = "Bisexual Colors"
                if randomint3 == 1:
                    randomint4 = random.randint(0,2)
                    if randomint4 == 0:
                        colort = 23
                        colorn = "Non-Binary Colors"
                    if randomint4 == 1:
                        colort = 24
                        colorn = "Asexual Colors"
                    if randomint4 == 2:
                        randomint5 = random.randint(0,1)
                        if randomint5 == 0:
                            colort = 25
                            colorn = "Rainbow Colors"
                        if randomint5 == 1:
                            colort = 26
                            colorn = "Transparent"

    if topt == 0 and bodyt == 0:
        colorimg = Image.open(PATH + "/color/2top/connected/" + str(colort) + ".png").convert(mode="RGBA")
    if topt == 0 and bodyt == 1:
        colorimg = Image.open(PATH + "/color/2top/float/" + str(colort) + ".png").convert(mode="RGBA")
    if topt == 1 and bodyt == 0:
        colorimg = Image.open(PATH + "/color/3top/connected/" + str(colort) + ".png").convert(mode="RGBA")
    if topt == 1 and bodyt == 1:
        colorimg = Image.open(PATH + "/color/3top/float/" + str(colort) + ".png").convert(mode="RGBA")

def BGTrait():
    global bgt
    global bgn
    global bgimg
#    bgt = random.randint(0,31)
    bgt = random.randint(0,5)
    bgn = str(bgt)
    bgimg = Image.open(PATH + "/background/" + str(bgt) + ".png").convert(mode="RGBA")

def WearTrait():
    global weart
    global wearn
    global wearimg
    weart = random.randint(0,31)
    wearn = str(weart)
    if bodyt == 0:
        wearimg = Image.open(PATH + "/wear/connected/" + str(weart) + ".png").convert(mode="RGBA") 
    if bodyt == 1:
        wearimg = Image.open(PATH + "/wear/float/" + str(weart) + ".png").convert(mode="RGBA")
