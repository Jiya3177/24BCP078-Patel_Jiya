# function to create and return a list containing tuples of the form (x,x2,x3) for 
# all x between 1 and given ending value (both inclusive).

n = int(input("Enter the ending value: "))
def create_list_ending_at(n):
    return [(x,x**2,x**3) for x in range(1,n+1)]

print(create_list_ending_at(n))

