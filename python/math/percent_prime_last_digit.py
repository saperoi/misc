from primegen import *

def limdigit(n):
    p = primegen(n)
    c = len(p)
    _one = []
    _two = []
    _tre = []
    _for = []
    _fyv = []
    _six = []
    _sef = []
    _eit = []
    _nyn = []
    _zro = []

    for _ in range(len(p)):
        l = p[_] % 10
        if l == 1:
            _one.append(p[_])
        elif l == 2:
            _two.append(p[_])
        elif l == 3:
            _tre.append(p[_])
        elif l == 4:
            _for.append(p[_])
        elif l == 5:
            _fyv.append(p[_])
        elif l == 6:
            _six.append(p[_])
        elif l == 7:
            _sef.append(p[_])
        elif l == 8:
            _eit.append(p[_])
        elif l == 9:
            _nyn.append(p[_])
        elif l == 0:
            _zro.append(p[_])
    
    f = open("tests/percent_prime.txt", "a")
    f.write(str(n) + "; " + str(c) + "\n")
    f.write("1: " + str(100*len(_one)/c) + "; " + str(len(_one)) + "\n")
    f.write("2: " + str(100*len(_two)/c) + "; " + str(len(_two)) + "\n")
    f.write("3: " + str(100*len(_tre)/c) + "; " + str(len(_tre)) + "\n")
    f.write("4: " + str(100*len(_for)/c) + "; " + str(len(_for)) + "\n")
    f.write("5: " + str(100*len(_fyv)/c) + "; " + str(len(_fyv)) + "\n")
    f.write("6: " + str(100*len(_six)/c) + "; " + str(len(_six)) + "\n")
    f.write("7: " + str(100*len(_sef)/c) + "; " + str(len(_sef)) + "\n")
    f.write("8: " + str(100*len(_eit)/c) + "; " + str(len(_eit)) + "\n")
    f.write("9: " + str(100*len(_nyn)/c) + "; " + str(len(_nyn)) + "\n")
    f.write("0: " + str(100*len(_zro)/c) + "; " + str(len(_zro)) + "\n")
    f.write("\n")
    f.close()
limdigit(250000)