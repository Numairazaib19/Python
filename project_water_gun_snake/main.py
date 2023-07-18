import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "g":
            return True
        elif you == "w":
            return False
    elif comp == "g":
        if you == "w":
            return True
        elif you == "s":
            return False
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False 
        

print("Comp turn: Choose Snake(s), Water(w), Gun(g)?")
randNO = random.randint(1, 3)
if randNO == 1:
    comp = "s"
elif randNO == 2:
    comp = "g"
elif randNO == 3:
    comp = "w"
    

you = input("yours turn: Choose Snake(s), Water(w), Gun(g)?")

a = game(comp, you)


print(f"Comp chooses: {comp}")
print(f"you chooses: {you}")

if a == None:
    print("This game is a tie")
elif a:
    print("You win!")
else:
    print("You lose!")
    
