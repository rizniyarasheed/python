#more than one form or many form
#different behave

#1)method overloading
#2)method overriding
#3)operator overloading

##method overloading
#same method different number of arguments

class Maths:
    def add(self):
        print("inside no arg")

    def add(self,num1):
        print("inside one arg")

    def add(self,num1,num2):
        print("inside two arg")

m=Maths()
m.add(1,2)

#drawback ==only recently call method is perform