from re import *

regno=input("enter registration number:")
rule="kl\d{2}[a-zA-z]{2}\d{4}"

matcher=fullmatch(rule,regno)
if matcher==None:
    print("invalid  registration number ")
else:
    print("valid  registration number")