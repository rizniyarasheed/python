

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))


if((num1 > num2)&(num1 > num3)):
    print("num1 is highest")
    if(num2 > num3):
        print("the scnd largest is num2",num2)
    elif(num3>num2):
        print("the scnd largest is num3", num3)
    elif  num2==num3:
        print("num2,num3",num2,num3)

elif((num2 > num1)&(num2 > num3)):


     if (num1 > num3):
         print("the scnd largest is num1", num1)
     else:
         print("the scnd largest is num3", num3)

elif((num3>num1)&(num3>num2)):


     if(num1 > num2):
         print("the scnd largest is num1", num1)
     else:
         print("the scnd largest is num2", num2)