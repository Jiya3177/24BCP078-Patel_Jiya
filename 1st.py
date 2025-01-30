#Count how many vowels are there in a string. Accept the string from the user.

a = input("Enter a string: ")
def count_vowels():
    vowels = "aeiouAEIOU"
    count = 0

    for char in a:
        if char in vowels:
            count += 1
    return count

vowels_count = count_vowels()

print(f"the number of vowels is {vowels_count}")