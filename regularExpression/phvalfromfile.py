#self work

f=open("phonenumbers","r")
dict={}

for lines in f:
    numbers=lines.rstrip("\n").split(" ")


from re import *

phnum=input(numbers)
rule="(91)?\d{10}"

mathcher=fullmatch(rule,phnum)
if mathcher==None:
    print("invalid ph number")
else:
    print("valid ph number")