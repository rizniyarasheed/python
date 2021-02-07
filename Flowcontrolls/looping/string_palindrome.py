

name="Luminar"
#print(len(name))    #length of charecter
#for i in range(6,0,-1):     #length star to 1 amd index start to 0
 #   print(name[i])       #so name[7] illaa


length=len(name)-1  #6
revers=""
while(length>=0): #6>0
    revers+=name[length]  #name[6]=r
    length -= 1  # 6-1=5
print(revers,end="")  #r