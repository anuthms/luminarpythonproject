f=open("students.py","r")
students={}
for lines in f:
    id,name,total,course=lines.rstrip("\n").split(",")

    if id not in students:
          students[id]={"id":id,"name":name,"total":total,"course":course}
def print_students_data(**kwargs):
    id=kwargs["id"]
    if id in students:
        print(students[id]["name"])
        if("prop"in kwargs):
          prop=kwargs["prop"]
          print(students[id][prop])

print_students_data(id="1000",prop="course")