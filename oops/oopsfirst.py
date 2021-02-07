#class
#object
#reference

class Person:
    #methods
    def setPerson(self,name,age):
        self.age=age
        self.name=name

    def printPerson(self):
        print("name:",self.name)
        print("age:",self.age)


#we created a class person(self.name,self.age)
#setPerson() and printPerson() are methods
#then create object

obj=Person()
obj.setPerson("Rizniya",21)
obj.printPerson()

obj1=Person()
obj1.setPerson("Rashida",23)
obj1.printPerson()



