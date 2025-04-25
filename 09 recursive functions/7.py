# Write a recursive func to obtain average of all numbers present in a given list.


def average_recursive(lst, n=None):
    if n is None:
        n = len(lst)
    if n == 1:
        return lst[0]
    return (lst[n - 1] + (n - 1) * average_recursive(lst, n - 1)) / n

# Example usage:
numbers = [4, 8, 15, 16, 23, 42]
print("Average:", average_recursive(numbers))
