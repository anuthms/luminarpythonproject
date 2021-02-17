class Parent:
    def mobile(self):
        print("nokia1234")

class Child(Parent):
    def mobile(self):
        print("i phone 11")

c=Child()
c.mobile()
print(c)