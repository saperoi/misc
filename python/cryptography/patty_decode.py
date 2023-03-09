cyphertext = list(str(input("Text to decode: ")))

shift = {
'q': 'a', 'h': 'b', 'f': 'c', 'e': 'd',
'3': 'e', 'r': 'f', 't': 'g', 'y': 'h',
'8': 'i', 'u': 'j', 'i': 'k', 'o': 'l',
'k': 'm', 'j': 'n', '9': 'o', '0': 'p',
'1': 'q', '4': 'r', 'w': 's', '5': 't',
'7': 'u', 'g': 'v', '2': 'w', 'd': 'x',
'6': 'y', 's': 'z',
'b': ' ', ".": " ", "x": " ", "c": " ", "v": " ", "n": " ",
'z': ',', 'm': '.'}

plaintext = []
for i in range(len(cyphertext)):
    plaintext.append(cyphertext[i].replace(cyphertext[i], shift[cyphertext[i].lower()]))

plaintext = "".join(plaintext)

print(plaintext)
