#What is the sum of the digits of the number 2^1000?

lst=list(str(2**1000))
lst=[int(i) for i in lst]
sum_digits=sum(lst)
print(sum_digits)
