# If a positive integer is entered through the keyword, write a recursive function 
# to obtain the prime factors of the number

n = int(input("enter the number: "))
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
        if n > 1:
            factors.append(n)
    return factors

print(prime_factors(n))  