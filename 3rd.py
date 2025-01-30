#Accept two strings. Check whether one string is there in another string.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str2 in str1:
    print(str2,"is present in",str1)
else:
    print(str2,"is not present in",str1)

if str1 in str2:
    print(str1,"is present in",str2)
else:
    print(str1,"is not present in",str2)

