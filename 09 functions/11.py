# Write a function create_list() that creates and returns a list which is an 
# intersection of two lists passed to it.

lst1 = [11,10,31,21,8,99,8,102,304]
lst2 = [9,11,7,8,21,99,999]
def create_list(list1, list2):
    return [value for value in lst1 if value in lst2]

print("list 1: ",lst1)
print("list 2: ",lst2)
print("Intersection of list 1 and list 2: ",create_list(lst1,lst2))