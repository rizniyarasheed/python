lst=[1,2,3,4,5,6]
#def square(num):
#    return num**2
#
#sqlist=list(map(square,lst))#function,iterable
#print(sqlist)
#



#using lambda
sqlist=list(map(lambda num:num**2,lst))#function,iterable
print(sqlist)

#if comdition
#num<5 num-1   num<5 num+1 else 5

numlist=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
print(numlist)

#convert uppercase
#function==>"hello".lower()

names=["india","Pak","aus","eng","sa","srilanka"]

upplist=list(map(lambda name:name.upper(),names))
print(upplist)