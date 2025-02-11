# A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))

# Solution
list = [("nitya",), ("kartik",), ("vishal",),("mahir",) ,"jilu","prushti", "kajol", "naira"]

boys_count=0
girls_count=0
for ele in list:
    if isinstance(ele, tuple):
        boys_count +=1
    else:
        girls_count +=1

print("The number of boys:",{boys_count})
print("The number of girls:",{girls_count})


