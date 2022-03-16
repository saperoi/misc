import engine as w

maxguesses = 17

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



print("                        _                  _ _      ")
print("                       | |                | | |     ")
print("  _ __  _   _ _ __ ___ | |__   ___ _ __ __| | | ___ ")
print(" | '_ \\| | | | '_ ` _ \\| '_ \\ / _ \\ '__/ _` | |/ _ \\")
print(" | | | | |_| | | | | | | |_) |  __/ | | (_| | |  __/")
print(" |_| |_|\\__,_|_| |_| |_|_.__/ \\___|_|  \\__,_|_|\\___|")
print("                                                    ")
print("                                                    ")
print("Please enter your first guess. y = incorrect spot, G = correct spot, - = not in number")

def setup():
    hidden = w.secretWord(alpha, len(alpha), False)
    maxg = 6

    numberdle = w.Wordle(hidden, maxg, "numberdle", allowed = "0123456789")
    numberdle.wordle(alpha)

setup()

pp = True
while pp == True:
    choice = input("Want to play again? y/n    ")
    if choice == "y":
        setup()
    elif choice == "Y":
        setup()
    else:
        pp = False