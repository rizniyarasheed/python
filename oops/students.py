#object printing
class Students:
    def __init__(self,rol,name,course,total):
        self.course=course
        self.rol=rol
        self.name=name
        self.total=total

    def __str__(self):
        return self.name

obj=Students(100,"Rizniya","django",150)
obj1=Students(101,"Rashida","msc",140)
obj2=Students(102,"Aneesha","django",130)

slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
#print(slist)

for stud in slist:
    #print(stud)#obj=Students(100,"Rizniya","django",150)
    if stud.course=="django":
        print(stud.name)

#total of django stud
total=0
for stud in slist:
    if stud.course=="django":
        total+=stud.total
print(total)

