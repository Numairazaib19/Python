# EmployeeName --> PascalCase
# isNumeric, isFloat --> camelCase

class Number:
    def sum (self):
        return self.a + self.b
    
num = Number()
num.a = 20
num.b = 30
s = num.sum()
print(s)