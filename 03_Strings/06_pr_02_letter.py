letter = '''Dear <|Name>|
You are selected!
Date = <|Date|>'''


name = input("Enter a name: ")
Date= input("Enter a date: ")
letter = letter.replace("<|Name>|", name)
letter = letter.replace("<|Date|>", Date)
print(letter)