#What is the 10001st prime number?

# function to check if a number is prime
import itertools
def isPrime(n):
  count=0
  for i in range (2,n//2+1):
    if n%i==0:
      return False
    else:
      continue
  
  return True

p = 0
for x in itertools.count(1):
    if isPrime(x):
        if p == 10001:
            print(x)
            break
        p += 1

