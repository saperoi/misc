import pyfiglet
from colorama import init, Fore, Style
name = "De Slimste Mens"
Fores = [Fore.RED, Fore.GREEN]
questions = [
    "Hoe noem je het als je iemand uit een raam gooit? (werkwoord)",
    "Wat is een landengte in het Engels?",
    "Vaak opvallend verschijnsel.",
    "Iemand die niets weet is een ....?",
    "Gevuld zijn met intense maar onuitgesproken woede. (werkwoord)",
    "Iets dat te doen heeft met ontbijt? (bn) (archaïsch :) )",
    "Overvloed",
    "Een gierige persoon is een ..?",
    "Iets weerleggen in een dispuut. (Schotland) (wet) (werkwoord)",
    "Een attractieve fysieke attribuut."
]
answers = [
    "defenestrate",
    "isthmus",
    "phenomenon",
    "ignoramus",
    "seethe",
    "jentacular",
    "galore",
    "niggard",
    "redargue",
    "thew"
]
f = pyfiglet.Figlet(font='big')
print(f.renderText(name))
print("Nederlands-Engels vertalen editie")
print()
print()
score = 0
for i in range(len(questions)):
    print(str(i+1) + ": " + questions[i])
    answer = input("")
    if answer.lower() == answers[i].lower():
        score += 1
        print(Fores[1] + "Goed zo!" + Style.RESET_ALL)
    else:
        print(Fores[0] + "Fout!" + Style.RESET_ALL + "Het correct antwoord was: " + answer[i].upper())
    print()
    print("Score: " + str(score))
    print()
    print()
if score < 5: print("Er is nog werk aan de winkel. Herpak je!")
elif score < 8: print("Je bent op de goede weg.")
elif score < 10: print("Je bent er bijna.")
else: print("Proficiat, je bent De Slimste Mens ter Wereld!")
