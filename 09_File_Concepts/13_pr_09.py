with open("this.txt") as f:
    content1 = f.read()
with open("copy.txt") as f:
    content2 = f.read()
if content1 == content2:
    print("Yes both are same")
else:
    print("both are not same")
    