num1=int(input("n01"))
num2=int(input("n02"))

temp=num1 #10
num1=num2 #20
num2=temp #10

print(num1)
print(num2)

num1=num1+num2 #10+20=30
num2=num1-num2 #30-20=10
num1=num1-num2 #30-10=20

print(num1)
print(num2)