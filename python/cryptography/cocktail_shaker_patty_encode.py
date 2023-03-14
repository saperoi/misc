import math

plain = list(str(input("Text to encode: ")))

alphabet = list("abcdefghijklmnopqrstuvwxyz")

# alternates aaaaaa = zbycxd

cyp = ""
n = 0
for i in range(len(plain)):
    try:
        letterIndex = alphabet.index(plain[i].lower())
    except:
        cyp += plain[i]
        continue
    shift = math.ceil((n+1)/2)
    if n%2 == 0: #right!
        char = alphabet[(letterIndex + shift)%26]
    elif n%2 == 1: #left!
        char = alphabet[(letterIndex - shift)%26]
    if plain[i].lower() != plain[i]:
        cyp += char.upper()
    else:
        cyp += char
    n += 1

print(cyp)
# j krth stp xjyizhagbfce yjou. lai'cu cfygx vwis vtz ducc s bme auhh.
