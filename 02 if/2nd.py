#Print the largest and smallest value out of 2

a = float(input("enter a num: "))
b = float(input("enter a num: "))
c = float(input("emter a num: "))

if ( a > b and b > c ): 
    print( a , "is largest number" , c , "is smallest number")
elif( b > c and c > a):
    print(b , "is largest number", a, "is smallest number")
elif( c > a and a > b):
    print(c , "is largest number", b, "is smallest number")
elif( a > c and c > b ):
    print(a , "is largest number", b, "is smallest number")
elif( b > a and a > c ):
    print(b , "is largest number", c, "is smallest number")
elif( c > b and b > a ):
    print(c , "is largest number", a, "is smallest number")
else:
    print("a = b = c ")
