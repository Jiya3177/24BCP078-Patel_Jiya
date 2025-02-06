# Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. Replace the third element of odd integers with a list of 4 even integers. Flattern, sort and print the list. Provide appropriate message at each stage.

import random

odd = [random.choice(range(1,100,2)) for _ in range(5)]
print("list of odd integers" ,odd)

even = [random.choice(range(0,100,2)) for _ in range(4)]
print("even interger is",even)

odd[2] = even

print(odd)

new_lst = []
for ele in odd:
    if isinstance(ele,list):
        new_lst.extend(ele)
    else:
        new_lst.append(ele)

print(new_lst)

