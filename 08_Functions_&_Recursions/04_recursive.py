def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
    
a = factorial_iter(5)
print(a)



def factorial_recursive(n):
    if n == 1 or n ==0:
        return 1
    return factorial_recursive(n-1)*n
        
    
a = factorial_recursive(5)
print(a)