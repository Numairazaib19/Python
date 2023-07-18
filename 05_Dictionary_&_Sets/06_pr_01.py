myDict = {
         "grow" : "agay barhna",
         "magic" : "Jaduu",
         "language" : "Zuban",
         "head" : "Sir",
         "fan" : "phanka"
         
}
print("Options are ", myDict.keys())

a = input("Enter the English word: ")
print("the meaning of your word is: ", myDict[a])

# by using get so below line will not thrown an error if the key is not present it will returns none
#print("the meaning of your word is: ", myDict.get(a))