class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age =age
        self.salary = salary
    def getInfo(self):
        print(f"The name of programmer Working in {self.company} is {self.name}, the age is {self.age} and the salary is {self.salary}")
        
        
Person1 = Programmer("Person1" , 21 , 500)
Person2 = Programmer("Person2" , 19 , 600)
Person3 = Programmer("Person3" , 17 , 700)

Person1.getInfo()
Person2.getInfo()
Person3.getInfo()