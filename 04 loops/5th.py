#Generate all Pythagorean Triplets with side length <= 30

def generate_pythagorean_triplets(n):
    triplet = []
    for a in range(1, n+1):
        for b in range(a, n+1):
            c = (a**2 + b**2)**0.5
            if c == int(c) and c <= n:
                triplet.append((a, b, int(c)))
    return triplet
    
n = 30
triplets = generate_pythagorean_triplets(n)
print(f"Pythagorean triplets with side lengths <= {n}:")
for triplet in triplets:
    print(triplet)