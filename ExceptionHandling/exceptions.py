#a abnoraml situation code is known as exception in this situation prgrm automatocally terminate
#eg:1.division by zero
#num1=int(input())
#num2=int(input())
#
#res=num1/num2
#print("res=",res)
#print("i have one database transaction")
#print("i have file operations")

#eg:2.file not found error
#eg:3.lst=[1,2,3,4]  print(lst(8)) value does not index
#eg:4.type errors   int,str....

#Exception handling
#this error handling method is known as exception handling
#keywrods
#1.try
#2.except(python)    catch(in javan)
#3.finally

#TRY==>doubtful code try
#eg:
num1=int(input())
num2=int(input())
try:
    res=num1/num2
    print("res=",res)
except Exception as e:
    print("exception occured")
print("i have one database transaction")
print("i have file operations")
