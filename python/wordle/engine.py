import random
from re import A
import time
from colorama import init, Fore, Style

class Wordle():
    def __init__(self, hidden, max, name = "wordle", allowed = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890"):
        init()
        self.FORES = [Fore.WHITE, Fore.YELLOW, Fore.GREEN]
        self.secret = hidden
        self.maxguesses = max
        self.name = name
        self.allowed = allowed

    def getGuess(self, epsilon):
        flagChar = False
        flagLen = False
        flagDict = False
        word = input()

        while flagChar == False or flagLen == False or flagDict == False:
            if len(word) != len(self.secret):
                flagLen = False
                if len(word) > len(self.secret):
                    print("Guess is too long, please try again")
                    word = input()
                if len(word) < len(self.secret):
                    print("Guess is too short, please try again")
                    word = input()
            else:
                flagLen = True
                
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

            if word in epsilon:
                flagDict = True
            else:
                flagDict = False
                print("Invalid guess, please try again")
                word = input()

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
        print(self.name + " " + str(self.guesses) + "/" + str(self.maxguesses))
        for n in range(len(e)):
            print(e[n])
        print("Try for yourself at [ https://github.com/saperoi/misc/tree/main/python/wordle ]")

    def wordle(self, epsilon):
        starttime = time.time()
        lasttime = starttime
        i = 1
        Corr = self.nCopies(len(self.secret), "G")
        Corr = copyfix(Corr, True)
        emojis = []
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
            emojis.append(verdict)
            print(verdict)
            self.vflag = False
            if verdict2 == Corr:
                print("You won! The word was: " + self.secret)
                print("You guessed it in " + str(i) + " guesses, and took " + str(round((time.time() - lasttime), 2)) + " seconds.")
                self.vflag = True
                self.guesses = str(i)
                i = self.maxguesses
            i += 1
        if self.vflag == False:
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