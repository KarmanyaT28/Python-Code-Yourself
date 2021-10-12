# Object oriented programming starts

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

#Unique Emplyee objects created in this way

print(emp_1)
print(emp_2)


emp_1.first = 'Karmanya'
emp_1.last = 'Tyagi'
emp_1.email = 'info@karmanya.in'
emp_1.payscale = '6000000'

emp_2.first = 'New'
emp_2.last = 'Person'
emp_2.email = 'info@newperson.in'
emp_2.payscale = '00000000'

# Now these instances are having unique attributes to them

print(emp_1.email)
print(emp_2.email)


#This way is too long and boring 
