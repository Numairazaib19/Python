class Employee:
    company = "Googli"
    def getSalary(self):
        print("salary is 100K")
        
Nemo = Employee()
Nemo.getSalary()
#Employee.getSalary(Nemo)


class Employee:
    company = "Googli"
    def getSalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")
        
Nemo = Employee()
Nemo.salary = 10000000
Nemo.getSalary()   
#Employee.getSalary(Nemo)