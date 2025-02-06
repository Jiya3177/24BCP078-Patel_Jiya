# Generate 20 random integers and store them in a list. Accept a number from the user and print position of all occurrences of that number in the list.import random
import random
num = random.choice(range(0,21))
n =[]
for i in range(0, 21):
    n.append(random.randint(0, 21))
print(n)

u = int(input("Enter a number: "))
for i in range(0, 21):
    if n[i] == u:
        print("Number is present at position", i+1)
else:
    print("Number is not present in the list")