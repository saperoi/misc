import engine as w

alphalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/basic.txt"
gammalink = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
wordcount = 1
alpha = w.getList(alphalink)
gamma = w.getList(gammalink)
name = "CLIrdle"

def setup():
    hidden = []
    hidden.append(w.secretWord(alpha, len(alpha), False))
    for i in range(wordcount - 1):
        appo = ""
        while len(appo) != len(hidden[0]):
            appo = w.secretWord(alpha, len(alpha), False)
        hidden.append(appo)
        
    maxg = 5 + wordcount + max(0, len(hidden[0]) - 5)
    wordle = w.Wordle(hidden, maxg, name, colors = "colorblinddark")
    wordle.wordle(gamma)

setup()

pp = True
while pp == True:
    choice = input("Want to play again? y/n    ")
    if choice.lower() == "y" or choice.lower() == "yes":
        setup()
    else:
        pp = False
