l = [9, 10, 22, 67, 100, 12, 4]
max = l[0]
min = l[0]

for i in l:
    if i > max:
        max = i
    elif i < min:
        min = i
    
print(max, min)
        
    