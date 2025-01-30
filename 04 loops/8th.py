#Print factorial of a given number

n = int(input("Enter a number: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        c = n * factorial(n-1)
        return c
    
print(factorial(n))