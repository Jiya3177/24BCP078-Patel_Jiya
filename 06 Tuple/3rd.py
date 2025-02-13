# Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.
import random

c = [random.choice(range(1,31)) for i in range(50)]
c.sort()
print(c)

# removing all duplicated 
for i in range(0,len(c)):
    while True:
        if c.count(i) >= 2:
            c.remove(i)
        else:
            break
print(c)