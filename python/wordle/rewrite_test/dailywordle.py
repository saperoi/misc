import engine as w
import datetime

alphalink = "https://cdn.discordapp.com/attachments/947100010959470595/954346459283734528/nyt_words_alpha.txt"
gammalink = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
alpha = w.getList(alphalink)
gamma = w.getList(gammalink)
name = "Daily Wordle"

def setup():
    d1 = datetime.date(2021,5,19)
    apa = str(datetime.datetime.now())
    apa = apa.split(" ")
    apa = apa[0].split("-")
    d2 = datetime.date(int(apa[0]), int(apa[1]), int(apa[2]))
    d = d2 - d1
    d = int(d.days)
    n = (d - 31) % len(alpha)
    hidden = [alpha[n]]
    maxg = 6

    wordle = w.Wordle(hidden, maxg, name, hard = False, colors="colorblinddark")
    wordle.wordle(gamma)

setup()
print()
print()
print()
print()
input()