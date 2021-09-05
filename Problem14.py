#Which starting number, under one million, produces the longest chain?
def collatz(i):
  count=0
  while i>1:
    if i%2==0:
      i=i/2
      count+=1
    else:
      i=3*i+1
      count+=1
    if i==1:
      return count
max_count=0
max_num=0
for i in range (2,1000000):
  n=collatz(i)
  if n>max_count:
    max_count=n
    max_num=i
print(max_num)
