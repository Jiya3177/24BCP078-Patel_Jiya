#multiplication table of given num

num = int(input("Enter a number: "))

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

multiplication_table(num)  # calling the function