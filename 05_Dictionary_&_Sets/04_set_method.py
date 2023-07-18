# an empty set can be crate by usning below syntax
b = set()
print(type(b))
b.add("xyz")
b.add(66)
print(b)

# we cannot add list and dictionary in set
# But
# we can add tuple in set
# only hashable objects we used in sets    hashable= conents maynot change   ,    non hashable= contents may change

b.add((1,2,3))
print(b)

print(len(b)) # prints the length of this set
b.remove("xyz") # remove xyz from the set (removal of item)
print(b)

print(b.pop()) # remove random value in sets
print(b)

#print(b.clear())  # it will empty the whole set
#print(b)