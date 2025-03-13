# Write a program that defines a function called frequency() which computes the 
# frequency of words present in a string passed to it. The frequencies should be 
# returned in sorted order of words in the string

String = input()

def frequency(string):
    words = string.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return sorted(word_freq.items())

print(frequency(String))