myDict = {
         "fast" : "In a quick manner",
         "game" : "Fun",
         "marks" : 99,
         "myList" : [1, 2, "Num", 4],
         "anotherDict" : {"Firstname" : "Nemo"}, #nested dictionary
         1: 5
         #"Fast" : "very quickly"   # overwrite
}

print(myDict.keys())
print(type(myDict.keys())) # by default type is dict keys


print(myDict.values())
print(type(myDict.values())) # by default type is dict values

print(list(myDict.keys())) # you can convert into the list  # typecasting into list
print(list(myDict.values()))  # for values

print(myDict.items()) # show all (key, values) for all contents present in dictionary

print(myDict)
update_dict = {
              "computer" : "make our work easier",
              "father" : "Dad"
}
myDict.update(update_dict)
print(myDict)



# example 2
d2 = {
    "money" : 67,
    "mission" : "possible"
}

print(d2)
update_d2 = {
    "Friend" : "ship"
}

d2.update(update_d2)
print(d2)

# get method
print(myDict.get(1)) # print value associated with key 1


# DIFFERENCE BETWEEN (.get) and [] syntax
# case in which key is not present in the dictionary
print(myDict.get("fast1")) # return none
print(myDict["fast1"])   # throw error