number = int(input("Enter a number: "))
prime = True
for i in range (2, number):
    if (number%i == 0):
        prime = False
        break
if prime:   
        print("The given number is prime")
else:
        print("The given number is not a prime")
    
    
    

    