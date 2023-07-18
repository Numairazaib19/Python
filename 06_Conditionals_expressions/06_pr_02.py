Total = 300
sub1 = int(input("Enter sub1: "))
sub2 = int(input("Enter sub2: "))
sub3 = int(input("Enter sub3: "))

percentage = ((sub1 + sub2 + sub3)/300)*100
print(percentage)


if sub1 < 33 or sub2 < 33 or sub3 < 33:
    print('fail because percentage less than 33 in one of the subjects')
elif percentage<40:
    print("fail because percentage is less than 40")
else:
    print("Pass")
    