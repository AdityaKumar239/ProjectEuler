#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# idea is to find LCM of numbers 1 to 20
import numpy as np
#define function for LCM of numbers x,y

def find_lcm(x,y):
  if (x>y):
    numerator=x
    denominator=y
  else:
    numerator=y
    denominator=x

  remainder=numerator%denominator

  while (remainder!=0):
    numerator=denominator
    denominator=remainder
    remainder=numerator%denominator
  gcd=denominator
  lcm=int(int(x*y)/gcd)

  return lcm

lst=np.arange(1,21)
print(lst)
lcm=find_lcm(1,2)

for i in range (2,20):
  lcm= find_lcm(lcm,lst[i])


print(lcm)
