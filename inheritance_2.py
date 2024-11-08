class Person:
    def person_info(self,name):
        print("inside person class")
        print("name:",name)

class company:
    def company_info(self,company_name):
        print("inside company class")
        print("name:",company_name)

class Employee(Person,company):
    def Employee_info(self,salary):
        print("inside employee class")
        print("salary:",salary)
emp=Employee()
emp.person_info("jessa")
emp.company_info("google")
emp.Employee_info(12000)