class Employee:
    company = "Google"
    
    def showDetails(self):
        print("This is an Employee")
        
class Programmer(Employee):
    language = "Python"
    #company = "Youtube"
    
    def getLanguage(self):
        print(f"the language is {self.language}")
        
        
    def showDetails(self):
        print("This is a Programmer")

e = Employee()
print(e.company)
e.showDetails()
p = Programmer()
p.getLanguage()
p.showDetails()
print(p.company)