import random
import time
from colorama import init, Fore, Style

class Wordle():
    def __init__(self, hidden, max):
        init()
        self.FORES = [Fore.WHITE, Fore.YELLOW, Fore.GREEN]
        self.secret = hidden
        self.maxguesses = max

    def getGuess(self, epsilon, allowed = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890"):
        flagChar = False
        flagLen = False
        flagDict = False
        word = input()

        while flagChar == False or flagLen == False or flagDict == False:
            if len(word) != len(self.secret):
                flagLen = False
                if len(word) > len(self.secret):
                    print("Hash is too long, please try again")
                    word = input()
                if len(word) < len(self.secret):
                    print("Hash is too short, please try again")
                    word = input()
            else:
                flagLen = True
                
            flag01 = True
            for p in range(len(word)):
                if word[p] not in allowed:
                    flag01 = False
            if flag01 == False:
                flagChar = False
                print("Hash contains invalid characters, please try again")
                word = input()
            else:
                flagChar = True

            if word in epsilon:
                flagDict = True
            else:
                flagDict = False
                print("Invalid hash, please try again")
                word = input()

        return word

    def copyfix(aw):
        av = ""
        for z in range(len(aw)):
            av += aw[z]
        aw = list(av)
        return av, aw

    def nCopies(n, copy):
        res = []
        for _ in range(n):
            res.append(copy)
        return res

    def wordle(self, epsilon):
        starttime = time.time()
        lasttime = starttime
        i = 1
        Corr = self.nCopies(len(self.secret), "G")
        while i <= self.maxguesses:
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
                            scrtcop, scrtlistcop = self.copyfix(scrtlistcop)
            for j in range(len(self.secret)):
                if verdictl[j] == "":
                    verdictl[j] = self.FORES[0] + "-" + Style.RESET_ALL
                    verdictl2[j] = "-"
            for c in range(len(scrtcop)):
                verdict += verdictl[c]
                verdict2 += verdictl2[c]
            print(verdict)
            self.vflag = False
            if verdict2 == Corr:
                print("You won! The word was: " + self.secret)
                print("You guessed it in " + str(i) + " guesses, and took " + str(round((time.time() - lasttime), 2)) + " seconds.")
                self.vflag = True
                i = self.maxguesses
            i += 1
        if self.vflag == False:
            print("You lost :( The word was: " + self.secret)
        

def secretWord(alpha, n):
    g = random.randint(0, n)
    secret = alpha[g]
    return secret