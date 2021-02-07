#low 5 upp 50 print all prime numbers between 5 to 50

lowlimit=int(input("enter lowlimit:"))   #5
upplimit=int(input("enter upplimit:"))   #50

print("Prime numbers between", lowlimit, "and", upplimit, "are:")

for num in range(lowlimit, upplimit + 1):  #5,51 num=5,6
# all prime numbers are greater than 1
   flag = 0
   for i in range(2,num):      #(2,5),(2,6)
       if (num % i) == 0:  # 5%2==0,6%3==0
           flag = flag + 1
           break
       else:
           flag = 0
       if (flag == 0):
           print(num)  # 5