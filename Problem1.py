#Find the sum of all the multiples of 3 or 5 below 1000.
#initiate the sum of numbers divisible by 3 as 0
sum_div_by_3=0
for i in range (1000):
  if i%3==0:
    sum_div_by_3+=i
#initiate the sum of numbers divisible by 5 as 0
sum_div_by_5=0
for i in range (1000):
  if i%5==0:
    sum_div_by_5+=i  
#initiate the sum of numbers divisible by 15 as 0
sum_div_by_15=0
for i in range (1000):
  if i%15==0:
    sum_div_by_15+=i  
# find total sum of numbers divisible by 3 or 5
 
total_sum=sum_div_by_3+sum_div_by_5-sum_div_by_15
print(total_sum)
