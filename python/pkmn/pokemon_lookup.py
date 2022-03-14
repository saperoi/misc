import json

doc = open('list.json', 'r')
yassy = json.loads(doc.read())
doc.close()
keys = yassy.keys()

pkmn = ["charizard", "blastoise", "beedrill", "pidgeot", "arbok", "nidoqueen", "nidoking", "ninetales", "arcanine", "machoke", "machamp", "bellsprout", "weepinbell", "rapidash", "cloyster", "marowak", "hitmonchan", "lickitung", "rhydon", "kangaskhan", "scyther", "lapras", "ditto", "vaporeon", "mewtwo", "feraligatr", "umbreon", "ursaring", "houndoom", "miltank"]

flag = False
while flag == False:
    for id in keys:
        for i in range(len(pkmn)):
            if pkmn[i].lower() == yassy[id]['name'].lower():
                print("\"" + pkmn[i] + "\"'s Pokemon ID = " + str(yassy[id]['id']))
                flag = True