#child inherit parent features
#we can access parent using parent class name in child class

class Parent:
    def phone(self):
        print("i have samsung j7")

class Child(Parent):
    pass

c=Child()
c.phone()

print(c)
print(id(c))

#different type of inheritance
#parent-->child
#super-->sub
#base-->derived
