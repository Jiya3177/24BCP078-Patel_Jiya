#Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic

num = int(input("Enter a number: "))

# check for prime number
def is_prime(num):
    if num <= 1:  
        return False
    for i in range(2, num):  
        if num % i == 0:  
            return False
    return True  

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#check for perfect number

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
    
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

# check for Armstrong number
def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for i in range(num_len):
        digit = int(num_str[i])
        sum += digit ** num_len
        if sum == num:
            return True
        else:
            return False
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#check for palindrome number
def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False
if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

# check for automorphic number

def is_automorphic(num):
    square = num ** 2
    str_square = str(square)
    str_num = str(num)
    if str_square.endswith(str_num):
        return True
    else:
        return False

if is_automorphic(num):
    print(f"{num} is an automorphic number.")
else:
    print(f"{num} is not an automorphic number.")

