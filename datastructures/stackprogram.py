num=10
def change():
    num=5
    num*=4
    print(num)#20
change()
print(num)#10

#global declaration

num=10
def change():
    global num
    num=5
    num*=4
    print(num)#20
change()
print(num)#20

#------------------------------xxxxxx----------------------------

size=int(input("enter the size of stack:"))
top=0
stk=[]
n=1

def push():
    item=int(input("enter item:"))
    global top

    if (top<size):
        stk.insert(top,item)
        top += 1
    else:
        print(top)
        print("stack overflow")

def pop():
    global top
    top-=1

    if top<0:
        print("stack is empty")
    else:
        print(stk[top],"popped out")

def display():
    for i in range(0,top):
        print(stk[i])

while(n!=0):
    option=int(input("enter operation  press 1)push 2)pop 3)display"))
    if option==1:
        push()
    elif option==2:
        pop()

    elif option==3:
        display()

    n=int(input("do you want to continue press 0 for exit "))








