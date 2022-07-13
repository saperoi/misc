"""
-------------------

This is a quick math quiz game.

-------------------
"""

import random
import time

def addition():
    s = 0
    starttime = time.time()
    lasttime = starttime
    while(True):
        print("Score: " + str(s))
        a = random.randint(0, 5000)
        b = random.randint(0, 5000)
        c = a + b
        print("What is " + str(a) + " + " + str(b) + "? ")
        print()
        d = input()
        print()
        if(str(c) == str(d)):
            s += 1
            print("Correct")
        else:
            print("False, the correct answer was: " + str(c))
            if s > 0:
                s -= 1
        print('You took ' + str(round((time.time() - lasttime), 2)) + ' seconds.')
        print()
        print()
        lasttime = time.time()

def subtraction():
    s = 0
    starttime = time.time()
    lasttime = starttime
    while(True):
        print("Score: " + str(s))
        a = random.randint(0, 5000)
        b = random.randint(0, 5000)
        while a < b:
            b = random.randint(0, 5000)
        c = a - b
        print("What is " + str(a) + " - " + str(b) + "? ")
        print()
        d = input()
        print()
        if(str(c) == str(d)):
            s += 1
            print("Correct")
        else:
            print("False, the correct answer was: " + str(c))
            if s > 0:
                s -= 1
        print('You took ' + str(round((time.time() - lasttime), 2)) + ' seconds.')
        print()
        print()
        lasttime = time.time()

def multiplication():
    s = 0
    starttime = time.time()
    lasttime = starttime
    while(True):
        print("Score: " + str(s))
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = a * b
        print("What is " + str(a) + " * " + str(b) + "? ")
        print()
        d = input()
        print()
        if(str(c) == str(d)):
            s += 1
            print("Correct")
        else:
            print("False, the correct answer was: " + str(c))
            if s > 0:
                s -= 1
        print('You took ' + str(round((time.time() - lasttime), 2)) + ' seconds.')
        print()
        print()
        lasttime = time.time()

def roots():
    
    s = 0
    starttime = time.time()
    lasttime = starttime
    while(True):
        print("Score: " + str(s))
        a = random.randint(0, 10)
        b = random.randint(1, 5)
        c = a ** b
        print("What is " + str(b) + "th root of " + str(c) + "? ")
        print()
        d = input()
        print()
        if(int(a) == abs(int(d))):
            s += 1
            print("Correct")
        else:
            print("False, the correct answer was: " + str(a))
            if s > 0:
                s -= 1
        print('You took ' + str(round((time.time() - lasttime), 2)) + ' seconds.')
        print()
        print()
        lasttime = time.time()

# we aren't doing division or exponents.

print("1: addition")
print("2: subtraction")
print("3: multiplication")
print("4: roots")

i  = input()

if i == "1":
    addition()

elif i == "2":
    subtraction()

elif i == "3":
    multiplication()

elif i == "4":
    roots()
