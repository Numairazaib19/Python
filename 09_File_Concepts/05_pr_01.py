with open("poem.txt", "r") as f:
    a = f.read()
#print(a)
if "twinkle" in a.upper():
    print("Yes")
elif "TWINKLE" in a.upper():
    print("Yes")
else:
    print("No")