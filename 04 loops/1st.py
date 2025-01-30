# uppercase and lowercase 
def printalpha():
    ch = "A"
    i = 0
    while i < 26:
        print(ch, end = " ")
        ch = chr(ord(ch) + 1)
        i = i + 1
print("uppercase alphabets :")
printalpha()

print("") 

def printalpha():
    ch = "a"
    i = 0
    while i < 26:
        print(ch, end = " ")
        ch = chr(ord(ch) + 1)
        i = i + 1
print("lowercase alphabets:")
printalpha()  