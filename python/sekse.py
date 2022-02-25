

class Sekse:
    class gender:
        self = []
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
        xenic = ""q
    class romantic:
        self = []
        masc = ""
        fem = ""
        andro = ""
        xenic = ""
    
    def __init__(self, genl, orient, rom, genu = None):
        if genu == None:
            genu = genl
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

meirl = Sekse((0, 0, 0, 0), (100, 100, 100, 25), (100, 100, 100, 25),(100, 10, 100, 0))
print(meirl.gender.self)

