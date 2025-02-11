# Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees

T = [32, 212, 0,20.3]
C = []
for temp in T:
    C.append((temp - 32) * 5/9)

print(C)
