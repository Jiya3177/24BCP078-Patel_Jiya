# # Calculate interest where I = PRN/100.
# Input :  = 10000
#         R = 5
#         T = 5
# Output :2500.0
# We need to find simple interest on 
# Rs. 10,000 at the rate of 5% for 5 
# units of time.
p = float(input("principale value: "))
t = float(input("enter time: "))
n = float(input("the rate of interest is: "))
intrest = p * t * n / 100
print(intrest)