# Consider the following list: lst = ['madam','Python',"malayalam",12321]
# Write a program to print those strings which are palindromes

lst = ['madam', 'Python', 'malayalam', 12321]
is_palindrome = lambda x: str(x) == str(x)[::-1]
palindromes = list(filter(is_palindrome, lst))
print("Palindromes in the list:", palindromes)