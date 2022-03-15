import engine as w
import os
import requests

alphalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/basic.txt"
betalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/basic256.txt"
gammalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/giant256.txt"
global maxguesses
maxguesses = 17

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

r = requests.get(betalink)
betaf = open("b.txt", "wb")
betaf.write(r.content)
betaf.close()
betaf = open("b.txt", "r")
global beta
beta = betaf.readlines()
for i in range(len(beta)):
    beta[i] = beta[i].replace("\n", "")
betaf.close()
os.remove("b.txt")

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

print("      _           ___  _____   __  _      ")
print("     | |         |__ \\| ____| / / | |     ")
print("  ___| |__   __ _   ) | |__  / /_ | | ___ ")
print(" / __| '_ \\ / _` | / /|___ \\| '_ \\| |/ _ \\")
print(" \\__ \\ | | | (_| |/ /_ ___) | (_) | |  __/")
print(" |___/_| |_|\\__,_|____|____/ \\___/|_|\\___|")
print("                                          ")
print("                                          ")
print("Please enter your first hash. y = incorrect spot, G = correct spot, - = not in hash")

def setup():
    hidden, n = w.secretWord(alpha, len(alpha), True)
    hiddenHash = beta[n]
    #print(hidden)
    #print(hiddenHash)
    Sha256le = w.Wordle(hiddenHash, maxguesses, "sha256le")
    Sha256le.wordle(gamma)
    print("The decoded word was: " + hidden)

setup()

while True:
    choice = input("Want to play again? y/n")
    if choice == "y":
        setup()
    elif choice == "Y":
        setup()
    else:
        quit
