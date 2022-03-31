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
  for i in range(2, x+1):
    n = primecheck(i)
    if n != 0:
      primes.append(i)
  return primes

def pk(n):
  primes = primegen(n)
  for p in range(len(primes)):
    x = 0
    m = n
    while m >= 1:
      m = m/primes[p]
      x += 1
    if m == 1/primes[p]:
      return (primes[p], x-1)
  return (0,0)