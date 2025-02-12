# Remove empty tuple(s) from the list of tuple

list=[(),(9,8,0),(1,),()]

print(list)

for i in list:
    if len(i)==0:
        list.remove(i)

print(list)