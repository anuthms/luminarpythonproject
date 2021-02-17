class Parent:
    def m1(self):
        print("inside parent")

class Child():

    def m1(self):#
        print("inside child")

class SubChild(Child,Parent):#first in subchild then child and last in parent according to order

    def m3(self):
        print("inside sub child")

obj=SubChild()
obj.m3()
obj.m1()