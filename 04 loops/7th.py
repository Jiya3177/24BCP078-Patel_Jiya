#Print nCr and nPr

def function(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def nCr(n,r):
    if r > n:
        return 0
    return function(n) // (function(r) * function(n-r))

def nPr(n,r):
    if r > n:
        return 0
    return function(n) // function(n-r)

n = int(input("Enter a value for n: "))
r = int(input("Enter a value for r: "))

print(f"{n}C{r} = {nCr(n,r)}")
print(f"{n}P{r} = {nPr(n,r)}")