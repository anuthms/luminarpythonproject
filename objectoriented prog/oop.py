#class
#object
#referance
class person:
    #methods
    def setPerson(self,age,name):
        self.age=age
        self.name=name

    def printperson(self):
        print("name=",self.name)
        print("age=",self.age)
    obj=Person()
    obj.setPerson(25,"ajay")
    obj.printPerson()