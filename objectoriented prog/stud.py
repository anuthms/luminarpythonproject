class Student:
    def set_student(self,rol,course,name):
        self.rol=rol
        self.course=course
        self.name=name

    def get_student(self,):
        print(self.rol,",",self.course,",",self.name)
obj=Student()
obj.set_student(1001,"django","anu")
print(obj.course)
print(obj.rol)
print(obj.name)