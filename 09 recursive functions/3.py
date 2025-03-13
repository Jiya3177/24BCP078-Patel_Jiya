# A string is entered through the keyboard. Write a recursive function that counts 
# the number of vowels in this string.

str = input("Enter the string: ")
def count_vowels(str):
    for i in str:
        if i in 'aeiouAEIOU':
            return  count_vowels(str[1:])
        else:
            return count_vowels(str[1:])

print(count_vowels(str))  

