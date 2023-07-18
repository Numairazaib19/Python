a = "The sky is blue"
s = a.split()
s = s[::-1]
s = " ".join(s)
print(s)


str1 = "apples@ and found^^  green&blue"
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''""

for i in str1:
    if i in punc:
        str1 = str1.replace(i, "")
print(str1)

