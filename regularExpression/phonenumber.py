from re import *

phno=input("enter phone number:")
rule="(91)?\d{10}"

matcher=fullmatch(rule,phno)
if matcher==None:
    print("invalid phone number ")
else:
    print("valid  phone number")