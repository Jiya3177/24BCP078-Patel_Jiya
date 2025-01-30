#Generate N numbers of Fibonacci series

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

N = int(input("Enter last limit: "))
fib_numbers = fibonacci(N)
print(fib_numbers)
