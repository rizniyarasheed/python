

#num=int(input("enter the number :"))
#while(num>0):
 #   digit=num%10
  #  print(digit,end=" ")
   # num=num//10


#palindrom
#multiply with10+digit

num=int(input("enter the number :"))
res=0
while(num>0):
    digit=num%10
    res=res*10+digit
    num = num // 10
print("res=", res)


#string

#num=int(input("enter the number :"))
#res=""
#while(num>0):
   #digit=num%10
  #  res=res+str(digit)
   # print("res=",res)
    #num = num // 10