import engine as w

alphalink = "https://cdn.discordapp.com/attachments/947100010959470595/954346459283734528/nyt_words_alpha.txt"
gammalink = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
alpha = w.getList(alphalink)
gamma = w.getList(gammalink)
name = "quordle"
totalwords = 4

def wordgen():
    hidden = w.secretWord(alpha, len(alpha), False)
    while len(hidden) != 5:
        hidden = w.secretWord(alpha, len(alpha), False)
    return hidden

def setup():
    hidden = ""
    hidden += wordgen()
    hidden += " "
    hidden += wordgen()
    hidden += " "
    hidden += wordgen()
    hidden += " "
    hidden += wordgen()
    # maxg = 4 + max(2, (len(hidden)-5))  # 6 if <5, n+1 if >= 5
    # maxg = len(hidden) + 1  # n + 1
    # maxg = 6 + 1  # 6
    maxg = 6 - max(0, -(len(hidden)+5))  # x + 1 if <5, 6 if >= 5

    wordle = w.Wordle(hidden, maxg, name, totalwords)
    wordle.wordle(gamma)

setup()

pp = True
while pp == True:
    choice = input("Want to play again? y/n    ")
    if choice.lower() == "y" or choice.lower() == "yes":
        setup()
    else:
        pp = False
