# Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.

d ={
    "apple": 100,
    "banana": 80,
    "orange": 70,
}
e = {
    "apple": 1,
    "banana" : 2,
    "orange": 3
    } 

for key in d:
    if key in e:
        d[key] = d[key] * e[key]
    else:
        print("Item not found")
print(d)

print("Total bill is: ", sum(d.values())) 