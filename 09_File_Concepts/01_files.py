# use open function to read the content of a file
# f = open("sample.txt")   # by default the mode is read "r"
f = open("sample.txt", "r" )
# data = f.read(5)    # read starting five character
data = f.read()
print(data)
f.close()

