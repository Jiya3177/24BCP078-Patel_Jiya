# points lie on straight line
x1 = int(input("enter a x1: "))
x2 = int(input("enter a x2: "))
x3 = int(input("enter a x3: "))
y1 = int(input("enter a y1: "))
y2 = int(input("enter a y2: "))
y3 = int(input("enter a y3: "))
print("point 1 is",(x1,y1))
print("point 2 is",(x2,y2))
print("point 3 is",(x3,y3))
m1 = (y2 - y1)/(x2 - x1)
m2 =(y3 - y2)/ (x3 - x2)
if ( m1 == m2 ):
    print("all the 3 points falls on straight line")
else:
    print("all the 3 points does not falls on straight line")
    
