import random
import time
from colorama import init, Fore, Style

class Wordle():
    def __init__(self, hidden, max, name = "wordle", allowed = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN", hard = False):
        init()
        self.FORES = [Fore.WHITE, Fore.YELLOW, Fore.GREEN]
        self.secret = hidden
        self.maxguesses = max
        self.allowed = allowed
        self.mode = hard
        self.name = name
        if self.mode == True:
            self.name += " HARD"
            print("You are playing hard mode, meaning you're required to use letters you used before, and in the correct spot if it was earlier.")
            print("To change this, go to your file you're running this from (probably \"wordle.py\") and change the following line:")
            print("`hard = True` to `hard = False`")

    def getGuess(self, epsilon):
        flagChar = False
        flagLen = False
        flagDict = False
        flagHard = False
        word = input()

        while flagChar == False or flagLen == False or flagDict == False or flagHard == False:
            
            # flagLen

            if flagLen == True:
                continue
            elif len(word) != len(self.secret):
                l = list(word)
                flagLen = False
                if len(word) > len(self.secret):
                    print("Guess is too long, please try again")
                    flagChar, flagLen, flagDict, flagHard = (False, False, False, False)
                    word = input()
                if len(word) < len(self.secret):
                    print("Guess is too short, please try again")
                    flagChar, flagLen, flagDict, flagHard = (False, False, False, False)
                    word = input()
            else:
                flagLen = True
            
            # flagChar
            
            if flagChar == True:
                continue
            flag01 = True
            for p in range(len(word)):
                if word[p] not in self.allowed:
                    flag01 = False
            if flag01 == False:
                flagChar = False
                print("Guess contains invalid characters, please try again")
                flagChar, flagLen, flagDict, flagHard = (False, False, False, False)
                word = input()
            else:
                flagChar = True
                
            # flagDict
            
            if flagDict == True:
                continue
            if word in epsilon:
                flagDict = True
            else:
                flagDict = False
                print("Invalid guess, please try again")
                flagChar, flagLen, flagDict, flagHard = (False, False, False, False)
                word = input()
                
            # flagHard

            w, v = self.lastguess
            w = list(w)
            v = list(v)
            l = list(word)
            
            if flagHard == True:
                continue
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
                            flagChar, flagLen, flagDict, flagHard = (False, False, False, False)   
                            word = input()
                    elif w[i] not in word and v[i] != "-":
                        flagHard = False
                        print("You are missing letters")
                        flagChar, flagLen, flagDict, flagHard = (False, False, False, False)
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
                    w += "⬛"
                if l == "y":
                    w += "🟨"
                if l == "G":
                    w += "🟩"
            e.append(w)
        print()
        print()
        print(self.name + " " + str(self.guesses) + "/" + str(self.maxguesses) + "   " + str(self.timespent) + " s")
        for n in range(len(e)):
            print(e[n])
        print("Try for yourself at <https://github.com/saperoi/misc/tree/main/python/wordle>")


    def wordle(self, epsilon):
        starttime = time.time()
        lasttime = starttime
        i = 1
        Corr = self.nCopies(len(self.secret), "G")
        Corr = copyfix(Corr, True)
        emojis = []
        self.lastguess = ("", "")
        while i <= self.maxguesses:
            print("Guess " + str(i) + "/" + str(self.maxguesses))
            print("--------------")
            word = self.getGuess(epsilon)
            word = word.lower()
            word = list(word)
            scrtcop = self.secret
            scrtlistcop = list(scrtcop)
            verdict = ""
            verdict2 = ""
            verdictl = self.nCopies(len(self.secret), "")
            verdictl2 = self.nCopies(len(self.secret), "")
            greens = self.nCopies(len(self.secret), False)

            for j in range(len(self.secret)):
                if word[j] == scrtlistcop[j]:
                    verdictl[j] = self.FORES[2] + "G" + Style.RESET_ALL
                    verdictl2[j] = "G"
                    scrtlistcop[j] = "-"
                    greens[j] = True
            for j in range(len(self.secret)):
                if greens[j] == True:
                    continue
                elif word[j] in scrtcop:
                    for k in range(len(self.secret)):
                        if word[j] == scrtlistcop[k]:
                            verdictl[j] = self.FORES[1] + "y" + Style.RESET_ALL
                            verdictl2[j] = "y"
                            scrtlistcop[k] = "-"
                            scrtcop, scrtlistcop = copyfix(scrtlistcop)
            for j in range(len(self.secret)):
                if verdictl[j] == "":
                    verdictl[j] = self.FORES[0] + "-" + Style.RESET_ALL
                    verdictl2[j] = "-"
            for c in range(len(scrtcop)):
                verdict += verdictl[c]
                verdict2 += verdictl2[c]
            emojis.append(verdict2)
            self.lastguess = (word, verdict2)
            print(verdict)
            self.vflag = False
            if verdict2 == Corr:
                print("You won! The word was: " + self.secret)
                self.timespent = round((time.time() - lasttime), 2)
                print("You guessed it in " + str(i) + " guesses, and took " + str(self.timespent) + " seconds.")
                self.vflag = True
                self.guesses = str(i)
                i = self.maxguesses
            i += 1
        if self.vflag == False:
            self.timespent = "/./"
            print("You lost :( The word was: " + self.secret)
            self.guesses = "X"
        print("Share with your friends!")
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
