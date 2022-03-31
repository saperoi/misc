from primegen import *
import math

def chebyshev_1(x):
  primes = primegen(x)
  summed = 0
  for k in range(len(primes)):
    summed += math.log(primes[k], math.e)
  return summed

def chebyshev_2(x):
  primes = primegen(x)
  summed = 0
  for m in range(2, x+1):
    if m in primes:
      summed += math.floor(math.log(x, m)) * math.log(m, math.e)
  return summed

def epsi(x):
  return math.exp(chebyshev_2(x))

def vonmangoldt(n):
  m, k = pk(n)
  if (m, k) == (0, 0):
    return 0
  else:
    return math.log(m, math.e)

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
