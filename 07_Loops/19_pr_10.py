a = int(input("Enter the table no: "))
limit = int(input("Enter the ending limit: "))

for i in range(limit,0, -1):
    #print(a , "*" , i , "=", a*i)
    # print(str(a) + " * " + str(i) + " = "+ str(a*i))
    print(f"{a} * {i} = {a*i}")     # f string
    
