# Write a program to check whether a dictionary is empty or not


user_dict = {}
n = int(input("Enter the number of key-value pairs you want to add to the dictionary: "))

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

if len(user_dict) == 0:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.") 