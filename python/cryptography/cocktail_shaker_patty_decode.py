import math

cyp = list(str(input("Text to decode: ")))

alphabet = list("abcdefghijklmnopqrstuvwxyz")

# alternates aaaaaa = zbycxd

plain = ""
n = 0
for i in range(len(cyp)):
    try:
        letterIndex = alphabet.index(cyp[i].lower())
    except:
        plain += cyp[i]
        continue
    shift = math.ceil((n+1)/2)
    if n%2 == 0: #left!
        char = alphabet[(letterIndex - shift)%26]
    elif n%2 == 1: #right!
        char = alphabet[(letterIndex + shift)%26]
    if cyp[i].lower() != cyp[i]:
        plain += char.upper()
    else:
        plain += char
    n += 1

print(plain)
# j krth stp xjyizhagbfce yjou. lai'cu cfygx vwis vtz ducc s bme auhh.
