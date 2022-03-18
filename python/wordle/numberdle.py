import engine as w

maxguesses = 17
name = "numberdle"

alpha = []
for i in range(100000):
    j = str(i)
    if len(j) == 1:
        j = "0000" + j
    if len(j) == 2:
        j = "000" + j
    if len(j) == 3:
        j = "00" + j
    if len(j) == 4:
        j = "0" + j
    alpha.append(j)

def setup():
    hidden = w.secretWord(alpha, len(alpha), False)
    maxg = 6

    numberdle = w.Wordle(hidden, maxg, name, allowed = "0123456789")
    numberdle.wordle(alpha)

setup()

pp = True
while pp == True:
    choice = input("Want to play again? y/n    ")
    if choice.lower() == "y" or choice.lower() == "yes":
        setup()
    else:
        pp = False