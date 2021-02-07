class Employee():
    def set_employee(self,eid,name,desig,salary):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.salary=salary

    def get_employee(self):
        print(self.eid,",",self.name,",",self.desig,",",self.salary)

obj=Employee()
obj.set_employee(1001,"rizni","HR","35000")
obj.get_employee()

obj=Employee()
obj.set_employee(2001,"niya","Manager","45000")
obj.get_employee()



#using constuctor
class Employee:
    def __init__(self,id,name,design):
        self.id=id
        self.name=name
        self.design=design

    def print_emp(self):
        print(self.name,self.id,self.design)
    def __str__(self):
        return self.name


obj=Employee(100,"emp1","ba")
obj.print_emp()
print(obj)
