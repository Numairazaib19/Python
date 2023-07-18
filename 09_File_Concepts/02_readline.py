# read line function

f = open("sample.txt", "r" )
# read first line
data = f.readline()
print(data)

# read second line
data = f.readline()
print(data)

# # read Third line and ... so on
data = f.readline()
print(data)

f.close()
