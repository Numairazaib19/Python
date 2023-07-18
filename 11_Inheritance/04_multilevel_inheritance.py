# fetch data from the nearest parent

class Person:
    country = "Pakistan"
    City = "Karachi"
    
    def takeBreath(self):
        print("I am breathing..")
        
class Employee(Person):
    company = "Tech Soln"
    
    def getSalary(self):
        print(f"Salary is {self.salary}")
        
    def takeBreath(self):
        print("I am an Employee so I am Luckily breathing..")
        
class Programmer(Employee):
    company = "Fiverr"
    
    def __init__(self, salary):
        self.salary = salary
        
    def getSalary(self):
        print(f"Salary is {self.salary}")
        
    def takeBreath(self):
        print("I am a Programmer so I am breathing pythonnn..")
        
p = Person()
p.takeBreath()
# print(p.company)
e = Employee()
print(e.company)
e.takeBreath()
prg = Programmer(500)
print(prg.company)
prg.getSalary()
prg.takeBreath()

