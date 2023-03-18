#not actual code, just a model idea

class Sekse:
    class gender:
        class low:
            self = []
            masc = ""
            fem = ""
            andro = ""
            xenic = ""
        class upp:
            self = []
            masc = ""
            fem = ""
            andro = ""
            xenic = ""
    class orientation:
        self = []
        masc = ""
        fem = ""
        andro = ""
        xenic = ""
    class romantic:
        self = []
        masc = ""
        fem = ""
        andro = ""
        xenic = ""
    name = ""
    def __init__(self, name, genl, orient, rom, genu = None):
        if genu == None:
            genu = genl
        self.name = name
        self.gender.self = [genl, genu]
        self.gender.low.self = genl
        self.gender.upp.self = genu
        (self.gender.low.masc, self.gender.low.fem, self.gender.low.andro, self.gender.low.xenic) = genl
        (self.gender.upp.masc, self.gender.upp.fem, self.gender.upp.andro, self.gender.upp.xenic) = genu
        self.orientation.self = orient
        (self.orientation.masc, self.orientation.fem, self.orientation.andro, self.orientation.xenic) = orient
        self.romantic.self = rom
        (self.romantic.masc, self.romantic.fem, self.romantic.andro, self.romantic.xenic) = rom


    def __str__(self):
        return f'Sekse({self.gender.self})'

    def __repr__(self):
        return f"Sekse(Gender = {self.gender.low.self} ~ {self.gender.upp.self}, Sexuality = {self.orientation.self}, Romantic Orientation = {self.romantic.self})"

    def sexual(a: "Sekse", b: "Sekse"):
        mascatt = False
        fematt = False
        andratt = False
        xenatt = False
        if (b.gender.low.masc - 12.5) <= a.orientation.masc <= (b.gender.upp.masc + 12.5):
            mascatt = True
        if (b.gender.low.fem - 12.5) <= a.orientation.fem <= (b.gender.upp.fem + 12.5):
            fematt = True
        if (b.gender.low.andro - 12.5) <= a.orientation.andro <= (b.gender.upp.andro + 12.5):
            andratt = True
        if (b.gender.low.xenic - 12.5) <= a.orientation.xenic <= (b.gender.upp.xenic + 12.5):
            xenatt = True
        if mascatt == True and fematt == True and andratt == True and xenatt == True:
            print(a.name + " is sexually attracted to " + b.name)
            return True
        else:
            print(a.name + " is NOT sexually attracted to " + b.name)
            return False

    def romance(a: "Sekse", b: "Sekse"):
        mascatt = False
        fematt = False
        andratt = False
        xenatt = False
        if (b.gender.low.masc - 12.5) <= a.romantic.masc <= (b.gender.upp.masc + 12.5):
            mascatt = True
        if (b.gender.low.fem - 12.5) <= a.romantic.fem <= (b.gender.upp.fem + 12.5):
            fematt = True
        if (b.gender.low.andro - 12.5) <= a.romantic.andro <= (b.gender.upp.andro + 12.5):
            andratt = True
        if (b.gender.low.xenic - 12.5) <= a.romantic.xenic <= (b.gender.upp.xenic + 12.5):
            xenatt = True
        if mascatt == True and fematt == True and andratt == True and xenatt == True:
            print(a.name + " is romantically attracted to " + b.name)
            return True
        else:
            print(a.name + " is NOT romantically attracted to " + b.name)
            return False
