import engine as w

alphalink = "https://example.com/alpha.txt"
gammalink = "https://example.com/gamma.txt"
wordcount = 1
alpha = w.getList(alphalink)
gamma = w.getList(gammalink)
name = "wordle"

def setup():
    hidden = []
    for i in range(wordcount):
        hidden.append(w.secretWord(alpha, len(alpha), False))
    maxg = 5 + wordcount
    wordle = w.Wordle(hidden, maxg, name, colors = "colorblinddark")
    wordle.getColorOptions()
    wordle.wordle(gamma)

setup()

pp = True
while pp == True:
    choice = input("Want to play again? y/n    ")
    if choice.lower() == "y" or choice.lower() == "yes":
        setup()
    else:
        pp = False
