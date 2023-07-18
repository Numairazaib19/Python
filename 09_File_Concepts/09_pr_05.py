listt = ["donkey", "good", "home" ]


with open ("censor_file.txt") as f:
    content = f.read()
for word in listt:
    content = content.replace(word, "$$^#@#@#$^$")
    with open ("censor_file.txt", "w") as f:
        f.write(content)
    