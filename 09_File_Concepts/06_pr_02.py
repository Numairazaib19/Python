# def game():
#     return 100

# score = game()
# with open("hi_score.txt") as f:
#     hi_score = int(f.read())

# if hi_score<score :
#     with open ("hi_score.txt", "w") as f:
#         f.write(str(score))



def game():
    return 10000

score = game()
with open("hiscore.txt") as f:
    hiscoreStr = f.read()

if hiscoreStr == "" :
    with open ("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiscoreStr)<score :
    with open ("hiscore.txt", "w") as f:
        f.write(str(score))
        
