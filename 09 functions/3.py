# defines a function create_array() to create and return a 3D array whose 
# dimensions are passed to the function. Also initialize each element of this 
# aray to a value passed to the function. 

def create_array(a, b, c, n):
    array_3d = [[[n for _ in range(c)] for _ in range(b)] for _ in range(a)]
    return array_3d

c = int(input("enetr 3rd perameter: "))
dimentions = (3,4,c)
initial_value = input()

array_3d = create_array(*dimentions, initial_value)

for layer in array_3d:
    print(layer)