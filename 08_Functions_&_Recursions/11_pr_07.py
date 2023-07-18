# this = "     Nemo is a good girl    "
# print(this)   
# print(this.strip())  # remove extra spaces

def remove_and_strip(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "     Nemo is a good girl    "
n = remove_and_strip(this, "Nemo")
print(n)