import engine as w
import os
import requests

alphalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/basic.txt"
gammalink = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

r = requests.get(alphalink)
alphaf = open("a.txt", "wb")
alphaf.write(r.content)
alphaf.close()
alphaf = open("a.txt", "r")
global alpha
alpha = alphaf.readlines()
for i in range(len(alpha)):
    alpha[i] = alpha[i].replace("\n", "")
alphaf.close()
os.remove("a.txt")

r = requests.get(gammalink)
gammaf = open("g.txt", "wb")
gammaf.write(r.content)
gammaf.close()
gammaf = open("g.txt", "r")
gamma = gammaf.readlines()
for i in range(len(gamma)):
    gamma[i] = gamma[i].replace("\n", "")
gammaf.close()
os.remove("g.txt")

print("   _____ _      _____         _ _      ")
print("  / ____| |    |_   _|       | | |     ")
print(" | |    | |      | |  _ __ __| | | ___ ")
print(" | |    | |      | | | '__/ _` | |/ _ \\")
print(" | |____| |____ _| |_| | | (_| | |  __/")
print("  \\_____|______|_____|_|  \\__,_|_|\\___|") 
print("                                       ")
print("                                       ")
print("Please enter your first guess. y = incorrect spot, G = correct spot, - = not in word")

def setup():
    hidden = w.secretWord(alpha, len(alpha), False)
    # maxg = 4 + max(2, (len(hidden)-5))  # 6 if <5, n+1 if >= 5
    # maxg = len(hidden) + 1  # n + 1
    # maxg = 6 + 1  # 6
    maxg = 6 - max(0, -(len(hidden)+5))  # x + 1 if <5, 6 if >= 5

    print(len(hidden) + "letters")
    wordle = w.Wordle(hidden, maxg, "CLIrdle")
    wordle.wordle(gamma)

setup()

pp = True
while pp == True:
    choice = input("Want to play again? y/n    ")
    if choice == "y":
        setup()
    elif choice == "Y":
        setup()
    else:
        pp = False
