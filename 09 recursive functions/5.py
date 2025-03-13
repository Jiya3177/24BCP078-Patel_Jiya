# Calculate a^b where a and b received through the keyword using recursion

a = int(input("base number: "))
b = int(input("power: "))

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)


print(power(a, b))