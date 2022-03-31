from primegen import *
import math
import time

def chebyshev_1(x):
    primes = primegen(x)
    summed = 0
    for k in range(len(primes)):
        summed += math.log(primes[k], math.e)
    return summed

def vonmangoldt(n):
    m, k = pk(n)
    if (m, k) != (0, 0) and k >= 1:
        p = math.log(m, math.e)
    else:
        p = float(0)
    return p

def lcm(x, y):
    #not my code, math.lcm didnt exist????
        if x > y:    
                greater = x    
        else:    
                greater = y    
        while(True):    
                if((greater % x == 0) and (greater % y == 0)):    
                        lcm = greater    
                        break    
                greater += 1    
        return lcm
    
def LCM_rep(x):
    nums = []
    for i in range(x):
        nums.append(i+1)
    if len(nums) == 1: return nums[0]
    else:
        c = lcm(nums[0], nums[1])
        if len(nums) >= 2:
            for i in range(2, len(nums)):
                c = lcm(c, nums[i])
    
    return c

def chebyshev_2lcm(x):
    return math.log(LCM_rep(x), math.e)


def chebyshev_2(x):
    """
    primes = primegen(x)
    summed = 0
    for m in range(2, x+1):
        if m in primes:
            summed += math.floor(math.log(x, m)) * math.log(m, math.e)
    return summed
    """
    summed = 0
    for i in range(x):
        summed += vonmangoldt(i+1)
    return summed

def epsi(x):
    return math.exp(chebyshev_2(x))



b = 0
while True:
    try:
        m = epsi(b)
    except:
        m = "ERR"
    print(str(b) + " - " + str(m))
    b += 1