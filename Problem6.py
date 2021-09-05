#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import numpy as np

#sum of squares  of first n numbers

def sum_sq(n):
  a=(n*(n+1)*(2*n+1))/6
  return a

#square of sum of first n numbers

def sq_sum(n):
  b=((n*(n+1))/2)*((n*(n+1))/2)
  return b

#for n=100:

print(sq_sum(100)-sum_sq(100))
