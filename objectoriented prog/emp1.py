class Employee:
    def __init__(self,id,ename,designation,salary):
        self.id=id
        self.ename=ename
        self.designation=designation
        self.salary=salary

    def __str__(self):
        return self.ename

f=open("emplist.py","r")
emplist=[]
dev_sal=[]
for lines in f:
    id,ename,designation,salary=lines.rstrip("\n").split(",")
    emplist.append(Employee(id,ename,designation,int(salary)))
from functools import reduce
for employee in emplist:
    if employee.designation=="operator":
        dev_sal.append(employee.salary)
print(dev_sal)

high=int(reduce(lambda no1,no2:no1 if no1>no2 else no2,dev_sal))
low=int(reduce(lambda no1,no2:no2 if no1<no2 else no2,dev_sal))
print(low)
print(high)
