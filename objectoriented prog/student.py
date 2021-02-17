class Student:
    def __init__(self,rol,course,name,marks):
        self.rol=rol
        self.course=course
        self.name=name
        self.marks=marks
    def __str__(self,):
        return self.name

obj=Student(100,"anu","django",140)
obj1=Student(101,"ann","mean",150)
obj2=Student(102,"alby","django",140)

slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
marks=0
for stud in slist:
    #print(stud)
    if stud.course=="django":
        total+=stud.marks
print(marks)
