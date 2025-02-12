# Delete an element of a tuple

tup = (20,31,7,3)
print("Original tuple: ", tup)
t = list(tup)
t.remove(31)
tup = tuple(t)
print("Tuple after removing 31: ", tup) 