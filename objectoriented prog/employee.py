class Employee:
    def set_employee(self,id,ename,designation,salary):
        self.id=id
        self.ename=ename
        self.designation=designation
        self.salary=salary

    def get_employee(self):
        print(self.id,",",self.ename,",",self.designation,",",self.salary)
obj=Employee()
obj.set_employee(1000,"anu","operator",25000)
obj1=Employee()
obj1.set_employee(1001, "ann", "operator", 30000)
print(obj.ename)
print(obj1.salary)