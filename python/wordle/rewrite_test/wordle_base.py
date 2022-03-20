import engine as w

alphalink = "https://example.com/alpha.txt" # LINK TO A TXT LIST OF POSSIBLE SECRET WORDS
gammalink = "https://example.com/gamma.txt" # LINK TO A TXT LIST OF GUESSABLE WORDS, CAN BE SAME AS ALPHA
alphalink = "https://cdn.discordapp.com/attachments/947100010959470595/954346459283734528/nyt_words_alpha.txt"
gammalink = "https://cdn.discordapp.com/attachments/947100010959470595/954784115444547634/nyt_words_gamma.txt"
alpha = w.getList(alphalink) # IF YOU WANT THE LIST IN PYTHON ITSELF, YOU CAN WITH AN ARRAY
gamma = w.getList(gammalink) # LIKE ["shit", "fuck", "dick"]
name = "quordle" # NAME OF THE WORDLE CLONE GAME

def setup():
    hidden = []
    hidden.append(w.secretWord(alpha, len(alpha), False))
    hidden.append(w.secretWord(alpha, len(alpha), False))
    hidden.append(w.secretWord(alpha, len(alpha), False))
    hidden.append(w.secretWord(alpha, len(alpha), False))
    hidden = ['abuse', 'breed', 'drink', 'chuck']
    print(hidden)
    maxg = 6 # FORMULA FOR THE MAX AMOUNT OF ALLOWED GUESSES, USE len(hidden) AS AN X FOR DIFFERENT MAX GUESSES BASED ON WORD LENGTH
    wordle = w.Wordle(hidden, maxg, name, colors = "colorblinddark")
    # add allowed = "string of allowed characters" depending on your word list, add hard = True for hard mode
    wordle.wordle(gamma)

setup()

pp = True
while pp == True:
    choice = input("Want to play again? y/n    ")
    if choice.lower() == "y" or choice.lower() == "yes":
        setup()
    else:
        pp = False
