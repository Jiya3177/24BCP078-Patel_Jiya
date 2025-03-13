# Ignore spaces and case mismatch while checking for palindrome.

s = input("Enter a string : ")
s = s.replace(" ", "").lower() # Remove spaces and convert to lowercase
def ispalidrome():
    return s == s[::-1]

if ispalidrome():
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
