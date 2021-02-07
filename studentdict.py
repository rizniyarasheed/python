#print_data(rol=1000) print name of stu rol=1000
#print_data(rol=1001,property="course") #name ,course

f=open("students", "r")

students={}

for lines in f:
    id,name,total,course=lines.rstrip("\n").split(",")
    if(id not in students):
          students[id]={"id":id,"name":name,"total":total,"course":course}

print(students)

def print_student_data(**kwargs):
    id=kwargs["id"]

    if id in students:
        print(students[id]["name"])
        if "prop" in kwargs:
           prop=kwargs["prop"]
           print(students[id][prop])
        else:
            pass
    else:
        print("there is no students exist with this id")


print_student_data(id="1001",prop="course")