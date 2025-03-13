# Write a recursive function to obtain length of a given string.

s = input("enter the string: ")
def length_of_string(s):
    if not s:
        return 0
    else:
        return 1 + length_of_string(s[1:])
    
print(length_of_string(s))