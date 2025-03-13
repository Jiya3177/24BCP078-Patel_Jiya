# recursive function that reverses the list of numbers that it receive

lst = []
n=int(input("Enter the number of elements in list: "))
for i in range(n):
    x=int(input("Enter element: "))
    lst.append(x)
print("Given list is: ",lst)

def reverse_list(lst):
    if len(lst) == 0:
        return lst
    elif len(lst) == 1:
        return lst
    else:
        return [lst[-1]] + reverse_list(lst[:-1])
    
print("Reversed list is: ",reverse_list(lst)) 