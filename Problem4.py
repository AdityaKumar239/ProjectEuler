#Find the largest palindrome made from the product of two 3-digit numbers.
import numpy as np
# function to check palindrome
def checkPalindrome(num):
  temp=num
  rev=0
  
  while temp != 0:
    rev=(rev * 10)+(temp % 10)
    temp=temp//10
 
  if num==rev:
    return True

  else:
    return False

#generating product of all pairs of 3 digit numbers
set_num=[]
for i in range(100,1000):
  for j in range (100,1000):
    set_num.append(i*j)
np.sort(set_num)
print(set_num[len(set_num)-1])
#check for palindrome and save in new set
pali_set=[]

for i in set_num:
  if checkPalindrome(i)==True:
    pali_set.append(i)

np.sort(pali_set)
np.max(pali_set)
