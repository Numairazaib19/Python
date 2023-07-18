dic1 = {
    12: "Bananas",
    4: "Apples",
    13: "peaches",
    1: "lemon"
}

d = sorted(dic1.keys())
dic2 = {}
for i in d:
    dic2[i] = dic1[i]
print(dic2)