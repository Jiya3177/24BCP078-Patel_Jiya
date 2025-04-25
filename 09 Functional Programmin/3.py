# Generate the list of 10 different random numbers between -15 and 15. Create a new list by obtaining square of all numbers in a list

import random

random_list = random.sample(range(-15, 16), 10)

squared_list = list(map(lambda x: x ** 2, random_list))

print("Original list:", random_list)
print("Squared list:", squared_list)
