def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Wrong!!!!!")

a = increment('abcd')
#a = increment("6")
print(a)