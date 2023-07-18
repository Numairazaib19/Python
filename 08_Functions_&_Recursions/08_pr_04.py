def natural_recursive(n):
    
    if n == 0 :
        return 0
    else:
        return n + natural_recursive(n-1)
    


a = natural_recursive(4)
print(a)