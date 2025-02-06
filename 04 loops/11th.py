def factorial(n):
    """
    Calculate the factorial of a number.
    
    :param n: The number to calculate the factorial for.
    :return: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_sin(x, terms=10):
    result = 0.0
    for n in range(terms):
        numerator = (-1)**n * x**(2*n + 1)
        denominator = factorial(2*n + 1)
        result += numerator / denominator
    return result

# Example usage:
x = float(input("Enter the value of x in radians: "))
terms = int(input("Enter the number of terms to use in the series: "))

sin_x = calculate_sin(x, terms)
print(f"sin({x}) ≈ {sin_x}")