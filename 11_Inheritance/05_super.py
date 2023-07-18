# fetch data from the nearest parent

class Person:
    country = "Pakistan"
    City = "Karachi"
    
    def __init__(self):
        print("Initializing a person..\n")
        
    
    def takeBreath(self):
        print("I am breathing..")
        
class Employee(Person):
    company = "Tech Soln"
    
    def __init__(self): 
        super().__init__()
        print("Initializing an employee..\n")
    
    def getSalary(self):
        print(f"Salary is {self.salary}")
        
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am Luckily breathing..")
        
class Programmer(Employee):
    company = "Fiverr"
    
    def __init__(self, salary):
        self.salary = salary
        
    def getSalary(self):
        print(f"Salary is {self.salary}")
        
    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so I am breathing pythonnn..")
        
# p = Person()
# p.takeBreath()

e = Employee()
# e.takeBreath()

# prg = Programmer(500)
# prg.takeBreath()

