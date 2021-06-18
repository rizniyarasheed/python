#rules
#1. a...k first character must be an alphabet b/w a-k
#2. second must be a digit divisible by 3
#3. followed by any number of charecters

#fullmatch() function is used to find exact match

from re import *

varname=input("enter variable name:")
rule="[a-k][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,varname)
if matcher==None:
    print("invalid variable name")
else:
    print("valid variable name")
