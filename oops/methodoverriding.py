class Parent:
    def mobile(self):
        print("nokia 5520")

class Child(Parent):
    def mobile(self):
        print("iph 11")

obj=Child()
obj.mobile()

#object class
#default
class Parent:
    def mobile(self):
        print("nokia 5520")

c=Parent()
print(c)
#o/p==><__main__.Parent object at 0x000001F4F73D9400>

#if we want to print a definition in that object then we use  __str__() method
#print an object while printing object __str__() will invoke object

class Parent:
    def mobile(self):
        print("nokia 5520")
    def __str__(self):
        return("hello parent")

c=Parent()
print(c)

