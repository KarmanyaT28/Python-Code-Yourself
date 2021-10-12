class Person(object):

    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False



#Inherited class

class Employee(Person):
   
    # Here we return true
    def isEmployee(self):
        return True


emp = Person("anyone")  # An Object of Person
print(emp.getName(), emp.isEmployee())
   
emp = Employee("karmanya") # An Object of Employee
print(emp.getName(), emp.isEmployee())

