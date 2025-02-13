# Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve no

import random

lst = [random.randint(-100,100) for _ in range(30)]

postive = [num for num in lst if num > 0]
negative = [num for num in lst if num < 0]

print("random list",lst)
print("positive list",postive)
print("negative list",negative)