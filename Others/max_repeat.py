a = "idniivevvvviiv"
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
max_char = max(d,key=d.get)
print(str(max_char))
