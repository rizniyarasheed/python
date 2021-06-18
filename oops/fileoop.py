#1)print employee details whose designation developer

#2)no of employees as developer

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
sallist=[]

for lines in f:
    #1000,anoob,developer,2,25000
    eid,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(Employees(eid,name,desig,exp,salary))




#1===>print employee details whose designation developer
devop=list(filter(lambda emp:emp.desig=="developer",emplist))
for emp in devop:
    print(emp)




#2===> no of employees as developer
cnt=len(devop)
print(cnt)
#or if devop list does'nt create situation
cnt=len(list(filter(lambda emp:emp.desig=="developer",emplist)))
print(cnt)


#3===>print employee details who have highest salary
maxsal=max(list(map(lambda emp:emp.salary,emplist)))
print(maxsal)



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



