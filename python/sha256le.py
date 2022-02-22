from hashlib import sha256
import random
import os
from pyparsing import java_style_comment
import requests
import time

alphalink = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

maxguesses = 3

def secretW():
    r = requests.get(alphalink)
    alpha = open("w.txt", "wb")
    alpha.write(r.content)
    alpha.close()
    alpha = open("w.txt")
    secret = random.choice(alpha.readlines())
    secrethash = sha256(secret.encode('utf-8')).hexdigest()
    alpha.close()
    return secret, secrethash, list(secrethash)

def sha256le():
    starttime = time.time()
    lasttime = starttime
    secret, secrethash, hashlist = secretW()
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
        scrtlistcop = hashlist
        verdictl = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        verdict = ""
        for j in range(len(secrethash)):
            if word[j] == scrtlistcop[j]:
                verdictl[j] = "G"
                scrtlistcop[j] = "-"
            elif word[j] in scrtcop:
                flag2 = False
                for k in range(len(secrethash)):
                    if flag2 == True:
                        continue
                    if word[j] == scrtlistcop[k]:
                        verdictl[j] = "y"
                        scrtlistcop[k] = "-"
                        flag2 = True
                    k += 1
            else:
                verdictl[j] = "-"
        for c in range(64):
            verdict += verdictl[c]
        print(verdict)
        flag = False
        if verdict == "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG":
            print("You won! The Sha256le word was: " + secret)
            print("You guessed it in " + str(i) + " guesses, and took " + str(round((time.time() - lasttime), 2)) + " seconds.")
            flag = True
        i += 1
    if flag == False:
        print("You lost! The Sha256le word was: " + secret)
    print("The hash was: " + secrethash)
    choice = input("Want to play again? y/n")
    if choice == "y":
        sha256le()
    elif choice == "Y":
        sha256le()
    else:
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
