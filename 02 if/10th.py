# area of rectangle is greter then perimeter or not
l = int(input("enter length of rectangle :"))
b = int(input("enter breadth of rectangle: "))
p = 2 *(l+b)
a = l * b
print(a)
print(p)
if ( p < a ):
    print("area of rectangle is greter then perimeter")
else:
     print("perimeter of rectangle is greter then area")
