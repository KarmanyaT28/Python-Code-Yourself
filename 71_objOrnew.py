class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,first,last,payscale):#Constructor
        self.first = first
        self.last = last
        self.payscale = payscale
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps+=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def applyraise(self):
        self.payscale = int(self.payscale * self.raise_amount)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount


emp_1 = Employee('Karmanya','Tyagi',600000)
emp_2 = Employee('New','Person',0000000)
Employee.set_raise_amt(1.05)


print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
















































# # print(emp_1.fullname())
# # print(emp_2.fullname())

# # print(Employee.fullname(emp_1)) 
# # print(Employee.fullname(emp_2))

# # print(emp_1.email)
# # print(emp_2.email)

# print(emp_1.payscale)
# emp_1.applyraise()
# print(emp_1.payscale)


# # emp_1.raise_amount
# # Employee.raise_amount


# print("----------------------")

# Employee.raise_amount =1.05
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)

# # print(emp_1.__dict__)
# # print(emp_2.__dict__)


# # print(Employee.__dict__)


# print(Employee.num_of_emps)