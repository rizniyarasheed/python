from re import *

mailid=input("enter mail id:")

rule='[a-zA-Z.]*[\d]*@gmail.com'

matcher=fullmatch(rule,mailid)
if matcher==None:
    print("invalid mail id")
else:
    print("valid mail id")