
while (True):
    print("Press q to quit")
    a = input("Entera Number: ")
    if a == "q":
        break
    try:
        a = int(a)
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:
        print(f"your input resultant an error: {e}")
        
print("Thankyou")