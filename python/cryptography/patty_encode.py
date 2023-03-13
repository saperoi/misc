plaintext = list(str(input("Text to encode: ")))

shift = {
"a": "q", "b": "h", "c": "f", "d": "e",
"e": "3", "f": "r", "g": "t", "h": "y",
"i": "8", "j": "u", "k": "i", "l": "o",
"m": "k", "n": "j", "o": "9", "p": "0",
"q": "1", "r": "4", "s": "w", "t": "5",
"u": "7", "v": "g", "w": "2", "x": "d",
"y": "6", "z": "s",
" ": ".", ",": "z", ".": "m"
}

cyphertext = []
for i in range(len(plaintext)):
    cyphertext.append(plaintext[i].replace(plaintext[i], shift[plaintext[i].lower()]))

cyphertext = "".join(cyphertext)

print(cyphertext)
