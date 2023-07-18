def conversion():
    f = (c * (9/5)) + 32
    return f

c = int(input("Enter Celcius: "))
a = conversion()
print(a)
    
    
# user defined
def conversion(c):
    f = (c * (9/5)) + 32
    return f

a = conversion(5)
print(a)