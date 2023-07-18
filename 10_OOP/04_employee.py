# class attribute (directly associated with class)

class Employee:
    company = "Google"
    
person1 = Employee()
person2 = Employee()
print(person1.company)
print(person2.company)
Employee.company = "Youtube"
print(person1.company)
print(person2.company)

# instance attribute
class Employee:
    company = "Google"
    
person1 = Employee()
person2 = Employee()
person1.salary = 300
person2.salary = 400
print(person1.salary)
print(person2.salary)