#print even num
lst=[1,2,3,4,5,6]

even=list(filter(lambda num:num%2==0,lst))
print(even)

#odd numbers

odd=list(filter(lambda num:num%2!=0,lst))
print(odd)


#print country name starting with a

names=["india","Pak","aus","eng","sa","srilanka","auckland","indonesia"]

acountry=list(filter(lambda name:name[0]=="a",names))
print(acountry)

