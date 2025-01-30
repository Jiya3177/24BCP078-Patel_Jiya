#Write your own functions to convert all characters of a string into lower case/upper case/toggle case.

b = input("str: ")
def lower_case(b):
    a = ""
    for char in b:
        if 'A'<= char <= 'Z':
            a += chr(ord(char) + 32)
        else:
            a += char
    return a

def upper_case(b):
    a = ""
    for char in b:
        if 'a'<= char <= 'z':
            a += chr(ord(char) - 32)
        else:
            a += char
    return a

def toggle_case(b):
    a = ""
    for char in b:
        if 'A'< char < 'Z':
            a += chr(ord(char) + 32)
        elif 'a'< char < 'z':
            a += chr(ord(char) - 32)
        else:
            a += char
    return a

lower = lower_case(b)
upper = upper_case(b)
toggle = toggle_case(b)

print(lower)
print(upper)
print(toggle)