class Employee:
    company = "Googli"
    def getSalary(self, signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod           # no need to take self argument it works
    def greet():
        print("Good Morning, Madam")
    
Nemo = Employee()
Nemo.salary = 10000000
Nemo.getSalary("Thanks!")  #Employee.getSalary(Nemo)
Nemo.greet()  #Employee.greet(Nemo)