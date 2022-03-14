import engine as w
import os
import requests

alphalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/basic.txt"
betalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/basic256.txt"
gammalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/giant256.txt"
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

print("                                                                                           ")
print("           88                        ad888888b,  8888888888     ad8888ba,  88              ")
print("           88                       d8\"     \"88  88            8P'    \"Y8  88              ")
print("           88                               a8P  88  ____     d8           88              ")
print(",adPPYba,  88,dPPYba,   ,adPPYYba,       ,d8P\"   88a8PPPP8b,  88,dd888bb,  88   ,adPPYba,  ")
print("I8[    \"\"  88P'    \"8a  \"\"     `Y8     a8P\"      PP\"     `8b  88P'    `8b  88  a8P_____88  ")
print(" `\"Y8ba,   88       88  ,adPPPPP88   a8P'                 d8  88       d8  88  8PP\"\"\"\"\"\"\"  ")
print("aa    ]8I  88       88  88,    ,88  d8\"          Y8a     a8P  88a     a8P  88  \"8b,   ,aa ")
print("`\"YbbdP\"'  88       88  `\"8bbdP\"Y8  88888888888   \"Y88888P\"    \"Y88888P\"   88   `\"Ybbd8\"'  ")
print("                                                                                           ")
print("Please enter your first hash. y = incorrect spot, G = correct spot, - = not in hash")

hidden, n = w.secretWord(alpha, len(alpha), True)
hiddenHash = beta[n]
#print(hidden)
#print(hiddenHash)
Sha256le = w.Wordle(hiddenHash, 17)
Sha256le.wordle(gamma)
print("The decoded word was: " + hidden)
while True:
    choice = input("Want to play again? y/n")
    if choice == "y":
        Sha256le.wordle(gamma)
    elif choice == "Y":
        Sha256le.wordle(gamma)
    else:
        quit