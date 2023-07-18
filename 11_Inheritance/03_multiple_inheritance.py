# multiple parents and one child

class Employee:
    company = "visa"
    eCode = 56
    
class Freelancer:
    company = "Fiverr"
    level = 0
    
    def upgradeLevel(self):
        self.level = self.level + 1
    
class Programmer(Employee, Freelancer):      # jo class pheel likhi hai uskay method func ko priority di jayegi
    name = "Nemo"
    
p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)
    