from tqdm import tqdm
#Find the sum of all the primes below two million.
import time
import math
start_time = time.time()
def isPrime(n):
  count=0
  for i in range (2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
    else:
      continue
  
  return True

sumPrime=0
for i in tqdm(range (3, 2000000,2)):
  if isPrime(i)==True:
    sumPrime+=i

print(sumPrime+2)
end_time = time.time()
print (end_time - start_time)
