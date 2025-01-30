# no of alphabets nd digits 

s = input("enetr string: ")
num_alpha = 0
num_digit = 0

for i in s:
    if i.isalpha():
        num_alpha += 1
    elif i.isdigit():
        num_digit += 1

print("Number of alphabets: ", num_alpha)
print("Number of digits: ", num_digit)

