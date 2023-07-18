a = input("Enter: ")

if ("make a lot of money" in a):
    spam = True
    
elif ("buy now" in a):
    spam = True
    
elif ("subscribe this" in a):
    spam = True

elif ("click this" in a):
    spam = True
    
else:
    spam = False
    

if(spam):
    print("This text is a Spam")
else:    
    print("This text is not a Spam")