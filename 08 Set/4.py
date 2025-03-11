# A set contains names which begin either with A or with B. Write a program to 
# separate out the names into two sets, one containing names beginning with A and 
# another with B.

set1 = { "arika","Ashmi","arjun","bansi","Big b","anuj","Banana","Apple","barfi","ac"}
print(set1)
setA = set()
setB = set()
for name in set1:
    if name[0] == 'A' or name[0] == 'a':
        setA.add(name)
    elif name[0] == 'B' or name[0] == 'b':
        setB.add(name)

print("Set A: ", setA)
print("Set B: ", setB)  