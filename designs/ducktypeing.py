class swift:
    def drive(self):
        print("driving swift car")
class sonet:
    def drive(self):
        print("driving sonet")

class Person:
    def start(self,car):
        car.drive()
sw=sonet()
p=Person()
p.start(sw)
