#check whether given num is divisible by 10 or not.

a = float(input("Enter a number: "))

if ( a % 10 == 0 and a != 0):
    print("The num",a," is divisible by 10")
elif ( not( a % 10 == 0 ) and a != 0):
    print("num" ,a ," is not divisible by 10")
else:
    print("Tne num is zero")
