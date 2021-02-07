class Parent:
    def m1(self):
        print("inside parent")
class Child:
    def m1(self):
        print("inside child")

class SubChild(Parent,Child):
    def m3(self):
        print("inside subchild")

obj=SubChild()
obj.m3()
obj.m1()