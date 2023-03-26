# Sets: unordered, mutable, no duplicates, (42:40) #

# myset = {1, 2, 3, 1, 2, 3} # print(myset) # {1, 2, 3} - no duplicates

# myset = set("Hello") # print(myset) # {'e', 'l', 'H', 'o'}

# myset = set() # creates empty set
# myset.add(1) # {1}
# myset.add(2) # {1, 2}
# myset.remove(2) # {1}
# myset.clear() # set() - empty set

# if 1 in myset:
#     print("yes")
# else:
#     print("no") # no

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)

print(diff)