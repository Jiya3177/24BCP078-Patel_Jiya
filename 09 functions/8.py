# removing all duplicate words and sorting them alphanumerically.


def convert(sentence):
    words = sentence.split()
    unique_words = sorted(set(words))
    result = " ".join(unique_words)
    
    return result 

sentence = input("Enter a sequence of whitespace-separated words: ")

result = convert(sentence)

print("String after removing duplicates and sorting:")
print(result)
