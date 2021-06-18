#print squares
lst=[10,20,30,40,50]

#squares=list(map(lambda num:num**2))
squares=[num**2 for num in lst]
print(squares)

#nested list
list=[[10,20],[30,40],[50,60]]

#print 10 20 30 40 50 60

#ls=[]
#for st in list:
#    for num in st:
#        ls.append(num)
#print(ls)

ls=[num for st in list for num in st ]
print(ls)

#(hw)find even numbers from given list using list comp
lt=[11,12,13,14,15,16,17]
evenls=[num for num in lt if num%2==0]
print(evenls)