#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
 
#store the fibobacci values under 4m in a dataset
import numpy as np
fib=np.zeros(32)
fib[0]=1
fib[1]=2
for i in range (2,32):
  fib[i]=fib[i-1]+fib[i-2]
#initial sum is set as 0
sum_fib_div_2=0
for i in range(32):
  if fib[i]%2==0:
    sum_fib_div_2+=fib[i]
sum_fib_div_2
