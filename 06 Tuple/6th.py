# Modify an element of a tupl

tup = (2,3,4,5)
print("tuple before modificaion:",tup)
l = list(tup)
# print(type(l))
l[0]=31
l[3]=20

tup = tuple(l)
print("tuple after modification:",tup)