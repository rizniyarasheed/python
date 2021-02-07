#1
#12
#123
#1234

#for row in range(1,5):     #1
 #   for col in range(row): #0,1
  #      print(col+1,end="")
   # print()


#another method

for row in range(1,5):       #1,2,3
    for col in range(1,row+1): #1,1+1=2  1,2,3   1,2,3,4
        print(col,end="")      #1        12          123
    print()

#1
#22
#333
#4444

for row in range(1,5):       #1,2,3
    for col in range(row+1): #0,1+1=2  0,1,2,3   0,1,2,3,4
        print(row,end="")    #11       222       3333
    print()