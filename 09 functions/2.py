def compute_series_sum(n):
    s = 0
    x = 0
    
    for i in range(n):
        x = x * 10 + n  # Constructing the number like 4, 44, 444, etc.
        s += x  
    
    return s

# Testing for n = 4 to 7
for i in range(4, 8):
    print(f"Sum for n = {i}: {compute_series_sum(i)}")