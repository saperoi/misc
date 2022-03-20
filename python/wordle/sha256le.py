import engine as w

alphalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/basic.txt"
betalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/basic256.txt"
gammalink = "https://raw.githubusercontent.com/saperoi/misc/master/src_files/dict/giant256.txt"
maxguesses = 17
name = "sha256le"

alpha = w.getList(alphalink)
beta = w.getList(betalink)
gamma = w.getList(gammalink)

def setup():
    hidden, n = w.secretWord(alpha, len(alpha), True)
    hiddenHash = [beta[n]]
    #print(hidden)
    #print(hiddenHash)
    Sha256le = w.Wordle(hiddenHash, maxguesses, name)
    Sha256le.wordle(gamma)
    print("The decoded word was: " + hidden)

setup()

pp = True
while pp == True:
    choice = input("Want to play again? y/n    ")
    if choice.lower() == "y" or choice.lower() == "yes":
        setup()
    else:
        pp = False