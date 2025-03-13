# Write a program that defines a function count_alpha_digits() that accepts a string 
# and calculates the number of alphabets and digits in it. It should return these 
# values as a dictionary.

s = input("enetr the string: ")
def count_alpha_digits(s):
    alpha_count = sum(1 for c in s if c.isalpha())
    digit_count = sum(1 for c in s if c.isdigit())
    return {'alpha_count': alpha_count, 'digit_count': digit_count}


print(count_alpha_digits(s))
