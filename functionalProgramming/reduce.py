#only one single output
#reduce fun is not directly get,it take from-->from functool import reduce

#print sum of lst

from functools import reduce

lst=[10,11,12,13,14]
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

#print highest num

high=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(high)

#lowest num

low=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(low)