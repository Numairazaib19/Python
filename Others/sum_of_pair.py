list = [8, 7, 2, 5, 3, 1]
l = len(list)
k = 10
for i in range(l):
    for j in range(i+1, l):
        if (list[i] + list[j] == k):
            print(list[i], list[j])
    