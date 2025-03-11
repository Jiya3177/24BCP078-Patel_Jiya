# create a set containing 10 random numbers in the range 15 to 45. Count how many 
# of these numbers are less than 30. Delete all numbers that are greater than 35.

import random
set1 = set()

set1 = {random.randint(15,45) for _ in range(11)}
print(set1)

s = 0
for i in set1:
    if i < 30:
        s += 1
print(s)

for i in list(set1):
    if i > 35:
        set1.remove(i)

print(set1)