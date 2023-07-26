class Class_name_1:
    def __init__(self, att1, att2): #constructor
        self.attribute1 = att1
        self.attribute2 = att2

#the constructor is called to create object1
object1 = Class_name_1(1, 1)

class Class_name_2: #type definition
    attribute3 = None
    attribute4 = Class_name_1(0, 0)

    def method1(self, parameter1):
        ...

    def __eq__(self, other): #overloads ==
        return (self.attribute3 == other.attribute3 and self.attribute4 == other.attribute4)

object2 = Class_name2() #generate object
object3 = Class_name2()
object2.attribute3 = 64 #write attribute
print(object_name.attribute1) #read attribute
object2 == object3 #True, uses overloaded ==
object2.method1(...) #call function 