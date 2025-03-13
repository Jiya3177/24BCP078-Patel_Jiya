# Pangram is a sentence that uses every letter of the alphabet. Write a program 
# to check whether a given string is pangram or not,


s = input("enter string: ")
def ispangram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(s.lower())

print(ispangram(s))