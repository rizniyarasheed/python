# read lower limit and upper limit
#print all even numbers from this lower limit upper limit
# 1 to 10

lowlimit=int(input("lower limt:"))
upperlimit=int(input("upper limit:"))
while(lowlimit<=upperlimit):
    if(lowlimit%2==0):
        print(lowlimit)
    lowlimit+=1