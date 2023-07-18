class Employee:
    company = "Google"
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")
        
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    
   
Nemo = Employee("Num" , 100000 , "Youtube")
#Nemo = Employee()  #--> this line throws an error (missing 3 required positional arguments: 'name', 'salary', and 'subunit')
Nemo.getDetails()