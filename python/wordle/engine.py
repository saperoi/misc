import random
import time
import requests
import os
import pyfiglet
from colorama import init, Fore, Style

class Wordle():
    def __init__(self, hidden: list, max: int, name: str = "wordle", allowed: str = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN", hard: bool = False, colors: str = "dark"):
        init()
        self.color_options = ["light", "dark", "colorblind", "colorblinddark", "text", "nerdle", "nerdlelight"]
        self.FORES = [Fore.WHITE, Fore.YELLOW, Fore.GREEN]
        self.secret = hidden
        self.wordcount = len(hidden)
        self.maxguesses = max
        self.allowed = allowed
        self.mode = hard
        self.name = name
        if colors not in self.color_options or colors == "light":
            self.colors = ["⬜","🟨","🟩"]
        if colors == "dark":
            self.colors = ["⬛","🟨","🟩"]
        if colors == "colorblind":
            self.colors = ["⬜","🟦","🟧"]
        if colors == "colorblinddark":
            self.colors = ["⬛","🟦","🟧"]
        if colors == "nerdle":
            self.colors = ["⬛","🟪","🟩"]
        if colors == "nerdlelight":
            self.colors = ["⬜","🟪","🟩"]
        if colors == "text":
            self.colors = ["-","y","G"]
        f = pyfiglet.Figlet(font='big')
        print(f.renderText(name))
        print("Please enter your first hash. y = incorrect spot, G = correct spot, - = not in hash")
        print()
        if self.mode == True:
            self.name += " HARD"
            print("You are playing hard mode, meaning you're required to use letters you used before, and in the correct spot if it was earlier.")
            print("To change this, go to your file you're running this from (probably \"wordle.py\") and change the following line:")
            print("`hard = True` to `hard = False`")
        print()
        if self.wordcount == 1:
            print("1 word of length " + str(len(self.secret[0])))
        else:
            print(str(len(self.secret)) + " words of length " + str(len(self.secret[0])))
        print()

    def getGuess(self, epsilon, guesslist):
        flagChar = False
        flagLen = False
        flagDict = False
        flagDeja = False
        flagHard = False
        word = input()

        while flagChar == False or flagLen == False or flagDict == False or flagDeja == False or flagHard == False:
            flagChar = False
            flagLen = False
            flagDict = False
            flagDeja = False
            flagHard = False
            length = len(self.secret[0])

            # flagLen

            if len(word) == length:
                flagLen = True
            else:
                l = list(word)
                flagLen = False
                if len(word) > length:
                    print("Guess is too long, please try again")
                    word = input()
                if len(word) < length:
                    print("Guess is too short, please try again")
                    word = input()
            
            # flagChar
            
            flag01 = True
            for p in range(len(word)):
                if word[p] not in self.allowed:
                    flag01 = False
            if flag01 == False:
                flagChar = False
                print("Guess contains invalid characters, please try again")
                word = input()
            else:
                flagChar = True
                
            # flagDict
            
            if word in epsilon:
                flagDict = True
            else:
                flagDict = False
                print("Invalid guess, please try again")
                word = input()
                
            # flagDeja
            
            if guesslist == []:
                flagDeja = True
            else:
                tempflagdeja = False
                for i in range(len(guesslist)):
                    if word == guesslist[i]:
                        tempflagdeja = True
                if tempflagdeja == False:
                    flagDeja = True
                else:
                    flagDeja = False
                    print("Already guessed this word")
                    word = input()

            # flagHard

            w, v = self.lastguess
            w = list(w)
            v = list(v)
            l = list(word)
            
            if self.mode == False:
                flagHard = True
            elif w == []:
                flagHard = True
            else:
                print(w)
                print(l)
                for i in range(len(w)):
                    vflagtemp = False
                    if v[i] == "G":
                        if w[i] != l[i]:
                            flagHard = False
                            vflagtemp = True
                            print("You are missing letters")
                            word = input()
                    elif w[i] not in word and v[i] != "-":
                        flagHard = False
                        print("You are missing letters")
                        word = input()
                    if vflagtemp == False:
                        flagHard = True

        return word

    def getColorOptions(self): print(self.color_options)

    def emojify(self, arr):
        e = []
        for p in range(len(arr)):
            g = list(arr[p])
            w = ""
            for k in range(len(g)):
                l = g[k]
                if l == "-":
                    w += self.colors[0]
                if l == "y":
                    w += self.colors[1]
                if l == "G":
                    w += self.colors[2]
                if l == " ":
                    w += " "
            e.append(w)
        print()
        print()
        print(self.name + " " + str(self.guesses) + "/" + str(self.maxguesses) + "   " + str(self.timespent) + " s")
        for n in range(len(e)):
            print(e[n])
        print("Try for yourself at <https://github.com/saperoi/misc/tree/main/python/wordle>")

    def getVerdict(self, guess, seca):
        sec = seca
        guessl = list(guess)
        verdict = []
        colorverdict = []
        arrverdict = []

        for _ in range(self.wordcount):
            sect = sec[_]
            secl = list(sect)
            tempverdict = nCopies(len(sect), "")
            tempcolorverdict = nCopies(len(sect), "")
            greens = nCopies(len(sect), False)

            for j in range(len(sect)):
                if guessl[j] == secl[j]:
                    tempcolorverdict[j] = self.FORES[2] + "G" + Style.RESET_ALL
                    tempverdict[j] = "G"
                    secl[j] = "-"
                    greens[j] = True
            for j in range(len(sect)):
                if greens[j] == True:
                    continue
                elif guessl[j] in sect:
                    for k in range(len(sect)):
                        if guessl[j] == secl[k]:
                            tempcolorverdict[j] = self.FORES[1] + "y" + Style.RESET_ALL
                            tempverdict[j] = "y"
                            secl[k] = "-"
                            sect, secl = copyfix(secl)
            for j in range(len(sect)):
                if tempverdict[j] == "":
                    tempcolorverdict[j] = self.FORES[0] + "-" + Style.RESET_ALL
                    tempverdict[j] = "-"
            arrverdict.append(copyfix(tempverdict, True))
            if _ != self.wordcount - 1:
                tempverdict.append(" ")
                tempcolorverdict.append(" ")
            tempverdict = copyfix(tempverdict, True)
            tempcolorverdict = copyfix(tempcolorverdict, True)
            verdict.append(tempverdict)
            colorverdict.append(tempcolorverdict)
        colorverdict = ArrToStrSpaces(colorverdict)
        verdict = ArrToStrSpaces(verdict)
        
        return verdict, colorverdict, arrverdict

    def wordle(self, epsilon):
        sec = []
        for _ in range(len(self.secret)):
            sec.append(self.secret[_])
        starttime = time.time()
        lasttime = starttime
        i = 1
        SpecCorr = []
        Blanks = []
        for _ in range(self.wordcount):
            _____ = ""
            ______ = ""
            for ___ in range(len(self.secret[_])):
                _____ += "G"
                ______ += "-"
            SpecCorr.append(_____)
            Blanks.append(______)

        emojis = []
        self.lastguess = ("", "")
        guesslist = []
        while i <= self.maxguesses:
            print("Guess " + str(i) + "/" + str(self.maxguesses))
            print("--------------")
            word = self.getGuess(epsilon, guesslist)
            word = word.lower()
            guesslist.append(word)
            word = list(word)

            verdict, colorverdict, arrverdict = self.getVerdict(word, sec)
            emojis.append(verdict)
            self.lastguess = (word, verdict)
            print(colorverdict)
            self.vflag = False
            
            for j in range(len(arrverdict)):
                if arrverdict[j] == SpecCorr[j]:
                    sec[j] = copyfix(nCopies(len(sec[j]), "-"), True)
                
            if sec == Blanks:
                if self.wordcount != 1:
                    print("You won! The was were: " + ArrToStrSpaces(self.secret))
                else:
                    print("You won! The word was: " + ArrToStrSpaces(self.secret))
                self.timespent = round((time.time() - lasttime), 2)
                print("You guessed it in " + str(i) + " guesses, and took " + str(self.timespent) + " seconds.")
                self.vflag = True
                self.guesses = str(i)
                i = self.maxguesses
            i += 1
        if self.vflag == False:
            self.timespent = "/./"
            if self.wordcount != 1:
                print("You lost :( The was were: " + ArrToStrSpaces(self.secret))
            else:
                print("You lost :( The word was: " + ArrToStrSpaces(self.secret))
            self.guesses = "X"
        print()
        print("Share with your friends!")
        print("Emoji's might show up as  ⍰  but they're still copyable")
        self.emojify(emojis)
        
def secretWord(alpha, n, bool = False):
    g = random.randint(0, n-1)
    secret = alpha[g]
    if bool == False: return secret
    return secret, g+1

def copyfix(aw, bool = False):
    av = ""
    for z in range(len(aw)):
        av += aw[z]
    aw = list(av)
    if bool == True: return av
    return av, aw

def getList(url):
    r = requests.get(url)
    urlf = open("temp.txt", "wb")
    urlf.write(r.content)
    urlf.close()
    urlf = open("temp.txt", "r")
    listi = urlf.readlines()
    for i in range(len(listi)):
        listi[i] = listi[i].replace("\n", "")
    urlf.close()
    os.remove("temp.txt")
    return listi

def ArrToStrSpaces(arr):
    stri = ""
    for i in range(len(arr)):
        stri += arr[i]
        if i != len(arr) - 1:
            stri += " "
    return stri

def nCopies(n, copy):
    res = []
    for _ in range(n):
        res.append(copy)
    return res