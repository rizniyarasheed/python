lst=[10,20,30]
pos=int(input("enter the position to print element:"))

num1=int(input("num1:"))
num2=int(input("num2:"))
try:
    res = num1 / num2
    print("res=", res)
    print(lst[pos])
except Exception as e:
    print(e.args)
