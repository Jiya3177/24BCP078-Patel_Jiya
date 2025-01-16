#Print the largest and smallest value out of 2
def ls2():
    a = float(input("enter a num: "))
    b = float(input("enter a num: "))
    #print("largest num is", a) if (a > b ) else print("largest num is ",b)
    if ( a > b ):
        print( a , " is largest number")
        print(b , "is smallest number")
    elif( a < b ):
        print(b , "is largest number")
        print(a , "is smallest number")
    else:
        print("a = b")
ls2()
