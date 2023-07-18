def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
    
item = int(input("Enter a number: "))

if item <0:
    print("please enter correct number")
else:
    for i in range(item):
        print(recur_fibo(i))
    
