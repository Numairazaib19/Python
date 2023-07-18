myDict = {
         "Fast" : "In a quick manner",
         "Game" : "Fun",
         "Marks" : 99,
         "MyList" : [1, 2, "Num", 4],
         "anotherDict" : {"Firstname" : "Nemo"}, #nested dictionary
         #"Fast" : "very quickly"   # overwrite
}

myDict["Marks"] = 100   # mutable
print(myDict)

print(myDict["Fast"])
print(myDict["Game"])
print(myDict["Marks"])
print(myDict["MyList"])
print(myDict["MyList"][2])
print(myDict["anotherDict"])
print(myDict["anotherDict"]["Firstname"])
