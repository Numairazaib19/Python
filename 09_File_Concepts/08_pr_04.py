with open ("censor_file.txt") as f:
    content = f.read()
    
content = content.replace("donkey", "$$^#@#@#$^$")
with open ("censor_file.txt", "w") as f:
    f.write(content)