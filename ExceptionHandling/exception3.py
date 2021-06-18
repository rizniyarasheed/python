#finally keyword is used to print mandatory part
num1=int(input("num1:"))
num2=int(input("num2:"))

try:
    res=num1/num2
    print(res)
except:
    num2 = int(input("num2:"))
    try:
        res = num1 / num2
        print(res)
    except:
      # print("exception occured")
      num2 = int(input("num2:"))
      res = num1 / num2
      print(res)
finally:
    print("i have one database transaction")
    print("i have file operations")

