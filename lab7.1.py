# Define the Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


person1 = Person("kriti", 19)
person2 = Person("mahit", 15)


person1.display()
person2.display()
