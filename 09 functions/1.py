# defines a function count_lower_upper() that accepts a string and calculates 
# the number of uppercase and lowercase alphabets in it. It should return these 
# values as a dictionary. Call this function for some sample string.

def count_lower_upper(str):
    lower = 0
    upper = 0
    for ch in str:
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
    return {'lower': lower, 'upper': upper}

str = input("Enter the string: ")
print(count_lower_upper(str)) 
print(type(str))

dict = dict(count_lower_upper(str))
print(dict)
print(type(dict))