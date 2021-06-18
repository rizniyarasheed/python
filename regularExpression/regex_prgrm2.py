#regular expression fundamentals

from re import *

#predefined charecter set

#pattern='[ab]' #this pattern means check for either a or b
#pattern="[a-z]" #check for lower case a to z
#pattern="[A-Z]"
#pattern="[a-bA-B]"#chech lower and upper
#pattern="[0-9]" #check for digits
#pattern="[^0-9]" #except 0-9
#pattern="[a-zA-Z0-9]"#except special charecters
#pattern="[^a-zA-Z0-9]"#only spl chsrecters




#predefined charecters

pattern="\s"  #chk for space
pattern="\S" #except space
pattern="\d" #chk for digit 0-9
pattern="\D" #except digit
pattern="\w" #chk for all words
pattern="\W" #except words


matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start(),"=>",match.group())#0 1
