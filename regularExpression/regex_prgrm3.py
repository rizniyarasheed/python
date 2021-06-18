#Quantifiers
from re import *

pattern="a+"# any number of 'a' excluding zero number of a
pattern="a*"#any number of 'a' including zero number of a
pattern="a?"#occurence of single 'a' including zero number of a
pattern="a{2}"# 2 number of a's
pattern="a{2,4}"#min 2 a and max 4 a

matcher=finditer(pattern,"aaaaaabbaabaaabbba")
for match in matcher:
    print(match.start(),"=>",match.group())