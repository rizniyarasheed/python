#chk given num is prime num or note
#num=7(1,7)   13(1,13)

num=int(input("enter number:"))
flag=0
if num==1:
    print("not prime")
else:
    for i in range(2, num):
        if (num % i == 0):
            # not prime
            flag = flag + 1
            break

        else:
            flag = 0
            # prime
    if flag == 0:
        print("prime")
    else:
        print("not prime")
