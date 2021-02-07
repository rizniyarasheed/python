
num=input("enter the number :") #"2"  #"3"
i=1                 #1,2 ,3   #1
data=0              #0,2,24   #0
pattern=""
while(i<=int(num)): #1<=2,2<=2,3<=2   #1<=3,2<=3,3<=3,4<=4
    res=num*i       #"2"*1=2,"2"*2=22   #"3"*1=3,"3"*2=33,"3"*3=333
    pattern=pattern+"+"+res   #+3   #+3+33   #+3+33+333
    data+=int(res)  #data=data+res  0+2=2,2+22=24  #0+3=3,3+33=36,36+333=369
    i+=1            #i=i+1  1+1=2,2+1=3       #1+1=2,2+1=3,3+1=4
pattern=pattern.lstrip("+")
print(pattern,end="")     #+3+33+333
print("=",data)         #2,24   #369

#2+22=24
