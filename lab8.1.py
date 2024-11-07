class Student:
    def __init__(self,name):

        print("inside constructor")
        self.name=name
        print("all initialized")

    def show(self):
        print(self.name)
s1=Student("emma")
s1.show()