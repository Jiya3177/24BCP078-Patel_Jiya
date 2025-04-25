# A list contains names of Faculty Members. Write a program to filter out those 
# names whose length is more than 8 characters.

faculty_names = ['Sanjanaaa', 'ankursing', 'Rahul', 'alok', 'Shivangi', 'darshit']
long_names = list(filter(lambda name: len(name) > 8, faculty_names))
print("Faculty members with more than 8 characters:", long_names)
