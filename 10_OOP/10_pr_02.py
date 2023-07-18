class Calculator:
    
    def __init__(self, num):
        self.number = num
        
    def square(self):
        print(f"The square of a {self.number} is {self.number**2}")
     
    def cube(self):
        print(f"The cube of a {self.number} is {self.number**3}")
        
    def sqaureroot(self):
        print(f"The square root of a {self.number} is {self.number**0.5}")
        
        
a = Calculator(3)
a.square()
a.cube()
a.sqaureroot()