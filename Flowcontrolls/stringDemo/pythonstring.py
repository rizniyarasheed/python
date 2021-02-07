#string is seqence of  characters
#how to represent string in python


#spliting string

name="Luminar Technolab Software Training institution"
words=name.split(" ")
print(words)


#print(name.upper()) #converting string into uppercase
#print(name.lower())  #converting string into lowercase


#removing character from begining
#print("name=",name.lstrip("Luminar"))

#removing character from begining
#print("name=",name.rstrip("tution"))

name=name.lstrip("Luminar")
print("name=",name)


