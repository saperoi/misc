import random
import time
import requests
import os
import pyfiglet
from colorama import init, Fore, Style

class Wordle():
    def __init__(self, hidden, max, name = "wordle", totalwords = 1, allowed = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN", colors = "light"):
        init()
        self.color_options = ["light", "dark", "colorblind", "colorblinddark", "text"]
        self.FORES = [Fore.WHITE, Fore.YELLOW, Fore.GREEN]
        self.wordcount = totalwords
        self.secretstr = hidden
        if self.wordcount == 1:
            self.secret = [hidden]
        else:
            self.secret = hidden.split(" ")
        self.maxguesses = max
        self.allowed = allowed
        self.mode = False
        self.name = name
        if colors not in self.color_options or colors == "light":
            self.colors = ["⬜","🟨","🟩"]
        if colors == "dark":
            self.colors = ["⬛","🟨","🟩"]
        if colors == "colorblind":
            self.colors = ["⬜","🟦","🟧"]
        if colors == "colorblinddark":
            self.colors = ["⬛","🟦","🟧"]
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

    def getColorOptions(self): print(self.color_options)

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

    def nCopies(self, n, copy):
        res = []
        for _ in range(n):
            res.append(copy)
        return res

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
        guessnn = ""
        guessnn += str(self.GuessN[0])
        for _ in range(len(self.GuessN) - 1):
            guessnn += " " + str(self.GuessN[_+1])
        print(guessnn)
        for n in range(len(e)):
            print(e[n])
        print("Try for yourself at <https://github.com/saperoi/misc/tree/main/python/wordle>")

    def wordle(self, epsilon):
        hidwords = self.secret
        starttime = time.time()
        lasttime = starttime
        emojis = ""
        i = 1
        Corr = ""
        SpecCorr = []
        BlankTrue = ""
        GuessTru = self.nCopies(self.wordcount, True)
        GuessFalse = self.nCopies(self.wordcount, False)
        self.GuessN = self.nCopies(self.wordcount, self.maxguesses + 1)
        for _ in range(self.wordcount):
            afytader = copyfix(self.nCopies(len(hidwords[_]), "G"), True)
            Corr += afytader
            SpecCorr.append(afytader)

        afytader = copyfix(self.nCopies(len(hidwords[0]), "-"), True)
        BlankTrue += afytader

        if self.wordcount != 1:
            for _ in range(self.wordcount - 1):
                afytader = copyfix(self.nCopies(len(hidwords[_ + 1]), "-"), True) + " "
            BlankTrue += afytader

        Corr = copyfix(Corr, True)
        emojis = []
        self.lastguess = ("", "")
        guesslist = []
        while i <= self.maxguesses:
            print("Guess " + str(i) + "/" + str(self.maxguesses))
            print("--------------")
            word = self.getGuess(epsilon, guesslist)
            word = word.lower()
            guesslist.append(word)
            gw = word
            for _ in range(len(word)-1):
                word += " " + gw
            word = list(word)

            colorverdict = []
            verdict = []
            arrverdict = []

            for w in range(self.wordcount):
                colorverdictt = ""
                verdictt = ""
                hidw = hidwords[w]
                hidl = list(hidw)
                print(hidw)
                print(hidl)

                for j in range(len(hidw)):
                    if word[j] == hidl[j]:
                        colorverdictt += self.FORES[2] + "G" + Style.RESET_ALL
                        verdictt += "G"
                        hidl[j] = "!"
                        hidw, hidl = copyfix(hidl)
                for j in range(len(hidw)):
                    for k in range(len(hidw)):
                        if word[j] == hidl[k] and j != k:
                            colorverdictt += self.FORES[1] + "!" + Style.RESET_ALL
                            verdictt += "!"
                            hidl[k] = "-"
                            hidw, hidl = copyfix(hidl)
                for j in range(len(hidw)):
                    if hidl[j] != "-":
                        colorverdictt += self.FORES[0] + "-" + Style.RESET_ALL
                        verdictt += "-"
                        hidw, hidl = copyfix(hidl)
                colorverdict.append(colorverdictt + " ")
                verdict.append(verdictt + " ")
                arrverdict.append(verdictt)
            
            colorverdict = copyfix(colorverdict, True)
            verdict = copyfix(verdict, True)
            emojis.append(verdict)

            print(colorverdict)

            if self.wordcount != 1:
                for ww in range(len(arrverdict)):
                    if arrverdict[ww] == SpecCorr[ww]:
                        GuessFalse[ww] = True
                        self.GuessN[ww] = i
                        hidwords[ww] = copyfix(self.nCopies(len(hidwords[ww]), "!"), True)
                        Corr = ""
                        SpecCorr = []
                        for _ in range(len(self.secret)):
                            afytader = copyfix(self.nCopies(len(hidwords[_]), "G"), True)
                            Corr += afytader
                            SpecCorr.append(afytader)
            self.vflag = False
            if verdict.replace(" ", "") == Corr or GuessFalse == GuessTru:
                print("You won! The word was: " + self.secretstr)
                self.timespent = round((time.time() - lasttime), 2)
                print("You guessed it in " + str(i) + " guesses, and took " + str(self.timespent) + " seconds.")
                self.vflag = True
                self.guesses = str(i)
                i = self.maxguesses
                    
            i += 1
        if self.vflag == False:
            self.timespent = "/./"
            print("You lost :( The word was: " + self.secretstr)
            self.guesses = "X"
            asasasasasaasasa = self.maxguesses + 1
            for g in range(len(self.GuessN)):
                if self.GuessN[g] == asasasasasaasasa:
                    self.GuessN[g] == "X"
        print()
        print("Share with your friends!")
        print("Emoji's might show up as ⍰ but they're still copyable")
        self.emojify(emojis)
        

def secretWord(alpha, n, bool = False):
    g = random.randint(0, n-1)
    secret = alpha[g]
    if bool == False: return secret
    return secret, g+1

def copyfix(aw, bool = False):
    av = ""
    for z in range(len(aw)):
        av += str(aw[z])
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
