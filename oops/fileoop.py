#print employee details whose designation developer

#no of employees as developer

#3)print employee details who have highest salary


class Employees:
    def __init__(self,eid,name,desig,exp,salary):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.name

f=open("employees.txt","r")
emplist=[]

for lines in f:
    #1000,anoob,developer,2,25000
    eid,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(Employees(eid,name,desig,exp,salary))

#for employee in emplist:
#    #print(employee)
#     if desig==developer:
#         developer+=developer
#print(employee.eid,employee.name,employee.salary,employee.exp)
#print(developer)
#
#3)=>
sallist=[]

for employee in emplist:
    sallist.append(employee.salary)
print(max(sallist))

#print highest sal employee name
for employee in emplist:
    sallist.append(employee.salary)
highsal=(max(sallist))

for employee in emplist:
    if employee.salary==highsal:
         print(employee)


#print lowest salary employee in developer name

for employee in emplist:
    sallist.append(employee.salary)
lowsal=(min(sallist))

for employee in emplist:
        if employee.salary==lowsal:
            print(employee)



