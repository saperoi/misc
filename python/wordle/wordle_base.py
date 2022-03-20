import engine as w

alphalink = "https://example.com/alpha.txt" # LINK TO A TXT LIST OF POSSIBLE SECRET WORDS
gammalink = "https://example.com/gamma.txt" # LINK TO A TXT LIST OF GUESSABLE WORDS, CAN BE SAME AS ALPHA
wordcount = 1 # amount of words you want
alpha = w.getList(alphalink) # IF YOU WANT THE LIST IN PYTHON ITSELF, YOU CAN WITH AN ARRAY
gamma = w.getList(gammalink) # LIKE ["shit", "fuck", "dick"]
name = "wordle" # NAME OF THE WORDLE CLONE GAME

def setup():
    hidden = []
    for i in range(wordcount):
        hidden.append(w.secretWord(alpha, len(alpha), False))
    maxg = 5 + wordcount # FORMULA FOR THE MAX AMOUNT OF ALLOWED GUESSES, USE len(hidden[0]) AS AN X FOR DIFFERENT MAX GUESSES BASED ON WORD LENGTH
    wordle = w.Wordle(hidden, maxg, name, colors = "colorblinddark")
    # add allowed = "string of allowed characters" depending on your word list, add hard = True for hard mode
    # un comment the next line to see all color options
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
