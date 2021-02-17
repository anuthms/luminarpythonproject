class Employee:
    def __init__(self,id,ename,designation,salary):
        self.id=id
        self.ename=ename
        self.designation=designation
        self.salary=salary

    def print_employee(self):
        print(self.id,",",self.ename,",",self.designation,",",self.salary)
#obj=Employee(1000,"anu","operator",25000)
#obj1=Employee(1001, "ann", "operator", 30000)
#obj.print_employee()
#obj1.print_employee()
