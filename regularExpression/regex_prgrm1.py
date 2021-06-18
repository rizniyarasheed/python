#reguler expression
#used to pattern matching
#not directly ge we have to import that re module
#step 1 import re module


from re import *

pattern="ab"


matcher=finditer(pattern,"ababababbbbaaababab")

cnt=0
print(matcher)
for match in matcher:
    print(match.start(),"'th position")
    print(match.group()) #ab ab ab
    cnt+=1
print("ab count=",cnt)