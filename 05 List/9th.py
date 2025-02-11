# Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension)

l1=[]
l2=[]
l3=[]
n=int(input("Enter the number of elements in list 1: "))
for i in range(n):
    x=int(input("Enter element: "))
    l1.append(x)
    
m=int(input("Enter the number of elements in list 2: "))
for i in range(m):
    y=int(input("Enter element: "))
    l2.append(y)
        
print("List 1: ",l1)
print("List 2: ",l2)

for num in l1:
    if num not in l2:
        l3.append(num)
        
print("List 3: ",l3)