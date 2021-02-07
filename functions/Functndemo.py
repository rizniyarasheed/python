
#print()  to print msg in console
#input()  to read value in console
#len()
#lstrip()
#rstrip()
#split()
#type()   to return variable type

#functions are used to perticualr task
#Bultinfunctions

#to call a function we use function_name()

#Create a function :-

#def function_name(parm1,parm2,parm3):
 #   functionDefintion
#function_name(argument)

def add(num1,num2):
    res=num1+num2
    print(res)
add(10,20)

#is argument nd parameter are same?
#A parameter is a variable listed inside the parentheses in the function defintion

#function with parm and not return values

add=lambda num1,num2:num1+num2
print(add(10,20))

def sub(num1,num2):
    result=num1-num2
    return result
data=sub(100,50)
print(data)