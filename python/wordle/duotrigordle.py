import engine as w

alphalink = "https://cdn.discordapp.com/attachments/947100010959470595/954346459283734528/nyt_words_alpha.txt"
gammalink = "https://cdn.discordapp.com/attachments/947100010959470595/954784115444547634/nyt_words_gamma.txt"
alpha = w.getList(alphalink)
gamma = w.getList(gammalink)
name = "duotrigordle"
totalwords = 32

def wordgen():
    hidden = ""
    while len(hidden) != 5:
        hidden = w.secretWord(alpha, len(alpha), False)
    return hidden

def setup():
    hidden = []
    for i in range(int(totalwords)):
        hidden.append(wordgen())
    
    # maxg = 4 + max(2, (len(hidden)-5))  # 6 if <5, n+1 if >= 5
    # maxg = len(hidden) + 1  # n + 1
    # maxg = 6 + 1  # 6
    maxg = 5 + totalwords  # x + 1 if <5, 6 if >= 5

    wordle = w.Wordle(hidden, maxg, name, colors = "dark")
    wordle.wordle(gamma)

setup()

pp = True
while pp == True:
    choice = input("Want to play again? y/n    ")
    if choice.lower() == "y" or choice.lower() == "yes":
        setup()
    else:
        pp = False
