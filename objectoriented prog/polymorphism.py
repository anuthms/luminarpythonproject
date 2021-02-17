#more than one form
#1) method overloading
class Maths:
    def add(self):
        print("inside no arg")

    def add(self,num1):
        print("inside one arg")

    def add(self,num1,num2):
        print("inside two arg")

m=Maths()
m.add(10,20)