# A positive integer is entered through the keyboard. Write a function to find its binary equivalent of this number.

def decimal_to_binary(n):
    if n <= 0:
        return "Enter a positive integer"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Example usage
num = int(input("Enter a positive integer: "))
print("Binary equivalent:", decimal_to_binary(num))
