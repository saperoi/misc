arr = [
'white_banner{BlockEntityTag:{Patterns:[{Color:5,Pattern:"vhr"},{Color:4,Pattern:"vh"},{Color:11,Pattern:"rs"},{Color:1,Pattern:"ls"},{Color:14,Pattern:"bo"}],id:"minecraft:banner"}}#§cR§r§6a§r§ei§r§an§r§bb§r§1o§r§5w§r §fFlag',
'white_banner{BlockEntityTag:{Patterns:[{Color:6,Pattern:"vhr"},{Color:6,Pattern:"vh"},{Color:0,Pattern:"cs"},{Color:3,Pattern:"bo"}],id:"minecraft:banner"}}#§bT§r§dr§r§fa§r§dn§r§bs§r §fFlag',
'white_banner{BlockEntityTag:{Patterns:[{Color:11,Pattern:"hhb"},{Color:2,Pattern:"hh"},{Color:10,Pattern:"ms"}],id:"minecraft:banner"}}#§dBis§r§5ex§r§9ual§r §fFlag',
'white_banner{BlockEntityTag:{Patterns:[{Color:10,Pattern:"vh"},{Color:15,Pattern:"ls"},{Color:4,Pattern:"rs"}],id:"minecraft:banner"}}#§8Non-§r§5Bi§r§fna§r§ery§r §fFlag',
'white_banner{BlockEntityTag:{Patterns:[{Color:4,Pattern:"hhb"},{Color:4,Pattern:"hh"},{Color:10,Pattern:"mc"},{Color:4,Pattern:"flo"}],id:"minecraft:banner"}}#§eInt§r§5er§r§esex§r §fFlag',
'white_banner{BlockEntityTag:{Patterns:[{Color:7,Pattern:"vhr"},{Color:15,Pattern:"rs"},{Color:10,Pattern:"ls"}],id:"minecraft:banner"}}#§5As§r§fex§r§7ua§r§8l§r §fFlag',
'white_banner{BlockEntityTag:{Patterns:[{Color:13,Pattern:"ls"},{Color:10,Pattern:"rs"}],id:"minecraft:banner"}}#§2Gend§r§ferq§r§5ueer§r §fFlag',
'white_banner{BlockEntityTag:{Patterns:[{Color:3,Pattern:"vh"},{Color:6,Pattern:"vhr"},{Color:4,Pattern:"cs"}],id:"minecraft:banner"}}#§bPan§r§esex§r§dual§r §fFlag',
'white_banner{BlockEntityTag:{Patterns:[{Color:8,Pattern:"vh"},{Color:10,Pattern:"cs"},{Color:15,Pattern:"tt"}],id:"minecraft:banner"}}#§8Dem§r§7is§r§5exu§r§fal§r §fFlag'
]


def colMatch(c):
    if c == "0":
        return "black"
    elif c == "1":
        return "dark_blue"
    elif c == "2":
        return "dark_green"
    elif c == "3":
        return "dark_aqua"
    elif c == "4":
        return "dark_red"
    elif c == "5":
        return "dark_purple"
    elif c == "6":
        return "gold"
    elif c == "7":
        return "gray"
    elif c == "8":
        return "dark_gray"
    elif c == "9":
        return "blue"
    elif c == "a":
        return "green"
    elif c == "b":
        return "aqua"
    elif c == "c":
        return "red"
    elif c == "d":
        return "light_purple"
    elif c == "e":
        return "yellow"
    elif c == "f":
        return "white"

#black_banner{display:{Name:'[{"text":"R","italic":false,"color":"dark_red"},{"text":"ainbow Flag","italic":false,"color":"dark_red"}]'}}
for stra in arr:
    a = stra.split('#')
    x = a[1]
    r = ""
    cols = x.replace("§r", "").split("§")
    cols.remove("")
    for i in range(len(cols)):
        r += '{"text":"' + cols[i][1:] + '","italic":false,"color":"' + colMatch(cols[i][0]) + '"},'
        if i == len(cols) - 1:
            r = r[:-1]
    t = "display:{Name:'[" + r + "]'}"
    print(a[0][:-1] + ',' + t + '}')
    print("\n")
