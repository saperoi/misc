from hashlib import sha256
import random
import os
import requests
import time
from colorama import init, Fore, Style

alphalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/basic256.txt"
betalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/giant256.txt"
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

init()
FORES = [Fore.WHITE, Fore.YELLOW, Fore.GREEN]

def freqtest(input_string):
    frequencies = {} 
  
    for char in input_string: 
        if char in frequencies: 
            frequencies[char] += 1
        else: 
            frequencies[char] = 1
    print(frequencies)

def secretW():
    g = random.randint(0, 849)
    secret = alpha[g]
    secrethash = beta[g]
    return secret, secrethash

def copyfix(aw):
    av = ""
    for z in range(len(aw)):
        av += aw[z]
    aw = list(av)
    return av, aw

def sha256le():
    starttime = time.time()
    lasttime = starttime
    secret, secrethash = secretW()
    i = 1
    while i <= maxguesses:
        word = input()
        while len(word) != 64:
            if len(word) > 64:
                print("Hash is too long, please try again")
                word = input()
            if len(word) < 64:
                print("Hash is too short, please try again")
                word = input()
        flag0 = True
        while flag0 == True:
            flag01 = True
            for p in range(len(word)):
                if word[p] not in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890":
                    flag01 = False
            if flag01 == False:
                print("Hash contains invalid characters, please try again")
                word = input()
            else:
                break
        word = word.lower()
        word = list(word)
        scrtcop = secrethash
        scrtlistcop = list(scrtcop)
        verdictl = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        greens = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        verdict = ""
        for j in range(len(secrethash)):
            if word[j] == scrtlistcop[j]:
                verdictl[j] = FORES[2] + "G" + Style.RESET_ALL
                scrtlistcop[j] = "-"
                greens[j] = True
        print(verdictl)
        for j in range(len(secrethash)):
            if greens[j] == True:
                continue
            elif word[j] in scrtcop:
                for k in range(len(secrethash)):
                    if word[j] == scrtlistcop[k]:
                        verdictl[j] = FORES[1] + "y" + Style.RESET_ALL
                        scrtlistcop[k] = "-"
                        scrtcop, scrtlistcop = copyfix(scrtlistcop)
        print(verdictl)
        for j in range(len(secrethash)):
            if verdictl[j] == "":
                verdictl[j] = FORES[0] + "-" + Style.RESET_ALL
        for c in range(len(scrtcop)):
            verdict += verdictl[c]
        print(verdict)
        flag = False
        if verdict == "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG":
            print("You won! The Sha256le word was: " + secret + "You guessed it in " + str(i) + " guesses, and took " + str(round((time.time() - lasttime), 2)) + " seconds.")
            flag = True
        i += 1
    if flag == False:
        print("You lost! The Sha256le word was: " + secret + "The hash was: " + secrethash)
    choice = input("Want to play again? y/n")
    if choice == "y":
        sha256le()
    elif choice == "Y":
        sha256le()
    else:
        os.remove("w.txt")
        quit
            
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
print("Also, there isn't any consideration yet for duplicate letters yet.")
print("Also also, capitals don't matter.")
sha256le()

#azertyuiopqsdfghjklmwxcvbnazertyuiopqsdfghjklmwxcvbn1234567890ab