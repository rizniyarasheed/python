class Student():
    def set_student(self,rol,name,course):
       self.rol=rol
       self.name=name
       self.course=course

    def get_student(self):
       print(self.rol,",",self.name,",",self.course)

obj=Student()
obj.set_student(101,"rizni","django")
obj.get_student()

#set_student()
#this method is performed by initializing instance variable
#instance variable are prepanded with self keyword
#
#we can access instance variable outside class by using reference
#
print(obj.course)
print(obj.rol)
#
#inside class self keyword


#constructor
#duty of constructor initializing instance variable
#constructor name always class name in java c++
#in python constuctor name is __init__()

#constructor automatically invoked during object creation
class Faculty():
    def __init__(self,rol,name,course):
        self.rol=rol
        self.name=name
        self.course=course

obj=Faculty(200,"Deepthi","bca")
print(obj.rol)
print(obj.name)
print(obj.course)