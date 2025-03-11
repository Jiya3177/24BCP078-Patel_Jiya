# Create an empty set. Write a program that adds five new names to this set, 
# modifies one existing name and deletes two names from it.

set1 = set()
print("Initial set: ", set1)

set1.update(["jilu","nishu","mahir","samay","naira"])
print("Set after adding names: ", set1)

if "samay" in set1:
    set1.remove("samay")
    set1.add("samarth")
print("Set after modifying name: ", set1)

set1.discard("mahir")
set1.discard("naira")
print("Set after deleting names: ", set1)  