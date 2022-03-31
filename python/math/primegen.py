def primecheck(x):
  flag = False
  for i in range(2, 1+x//2):
    if flag == True:
      break
    elif(x%i)==0:
      flag = True
      break
  if flag == False:
    return x
  else:
    return 0
    
def primegen(x):
  primes = []
  for i in range(2, x):
    n = primecheck(i)
    if i != 0:
      primes.append(x)
  return primes

def pk(n):
  primes = primegen(n)
  for p in range(len(primes)):
    x = 0
    m = n
    while m % primes[p] == 0:
      m = m/primes[p]
    if m == 1:
      return (primes[p], x)
  return (0,0)