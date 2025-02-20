# Write a program to create three dictionaries and concatenate them to create fourth dictionary.
#  take value from user and store it in dictionary
#  and then concatenate the three dictionaries to create fourth dictionary.

user_dict ={}

n = int(input("Enter the number of key-value pairs you want to add to the dictionary: "))

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print(user_dict)
d1={
    "a" : 1,
    "b" : 2,
    "c" : 3,
}

d2 = {
    "d" : 4,
    "e" : 5,
    "f" : 6,
}

d3={
    "g" : 7,
    "h" : 8,
    "i" : 9,
}

d4 = { **d1, **d2, **d3 }

print(d4)