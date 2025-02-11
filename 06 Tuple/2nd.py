# A list contains tuples containing roll no., name and age of student. Write a python program to create three lists separately for roll no., name and age

l = [(1233,"Megha",20),(1238,"Krupa",24), (9124,"Honey",18)]
roll_no = []
name = []
age = []
for i in l:
    roll_no.append(i[0])
    name.append(i[1])
    age.append(i[2])

print("Roll numbers:",roll_no)
print("Names:",name)
print("Ages:",age)