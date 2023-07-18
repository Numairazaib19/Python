class Employee:
    company = "Google"
    salary = 100
    
person1 = Employee()
person2 = Employee()

print(person1.salary)
print(person2.salary)

# below line throws an error as address instance is not present in class
#print(numaira.address)