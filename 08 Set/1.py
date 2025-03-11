# converts words present in a list into uppercase and stores them in a set

lst = ["apple","python","cricket","movies"]
set1 = set()
for word in lst:
    set1.add(word.upper())

print(set1)  