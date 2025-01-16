# If a point lies inside the circle, on the circle or outside the circle

def check_the_point(x0,y0,r,x,y):
    x0 = 0
    y0 = 0
    r = int(input("Enter radius of circle: "))
    x = int(input("Enter the x-coordinate of the point: "))
    y = int(input("Enter the y-coordinate of the point: "))

    distance = (((x - x0) ** 2 + (y - y0) ** 2) ** 0.5) 

    if distance < r:
        print ("Point lies Inside the circle")
    elif distance == r:
        print ("Point lies On the circle")
    else:
        print ("Point lies Outside the circle")

check_the_point(0,0,5,2,3)
