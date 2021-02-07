employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001 : {"id": 1001, "name": "jhon", "salary": 30000, "exp": 2},
    1002 : {"id": 1002, "name": "danie", "salary": 35000, "exp": 2},
    1003 : {"id": 1003, "name": "jack", "salary": 30000, "exp": 2},
}

#print(employee[1000]) #o/p=={'id': 1000, 'name': 'tom', 'salary': 25000, 'exp': 1}
#
##print name of employee who have id=1001
#if 1001 in employee:
#    print(employee[1001]["name"])
#else:
#    print("employe with id not exist")
#
#
## print salary of employee who have id=1003
#if 1003 in employee:
#    print(employee[1003]["salary"])
#else:
#    print("employe with id not exist")


#
def print_employee(id=None):
    if id in employee:
        print(employee[id]["name"])
    else:
        print("employe with this id not exist")

print_employee(id=1002) #o/p== danie



#using property
def print_employee(id=None,prop=None):
    if id in employee:
        print(employee[id][prop])
    else:
        print("employe with this id not exist")

print_employee(id=1000,prop="salary") #o/p==25000



#kwargs
def print_employee(**kwargs):
    print(kwargs)
    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
    else:
        print("employe with this id not exist")

print_employee(id=1000)



#kwargs 2 argument
def print_employee(**kwargs):

    id=kwargs["id"] #id=1000
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])#prop="exp"
        else:
            pass
    else:
        print("employe with this id not exist")

print_employee(id=1000,prop="exp")

