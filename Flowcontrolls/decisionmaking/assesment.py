#read two numbers
#print true if sum of two number equal to 100 or any one num is 100
#else print false


num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

if((num1+num2==100)|(num1==100)|(num2==100)):
    print("true")

else:
    print("false")