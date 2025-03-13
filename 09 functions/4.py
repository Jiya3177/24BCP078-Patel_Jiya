# defines a function sum_avg() to accept marks of five subjects and calculates 
# total and average. 

def sum_avg():
    s1 = float(input("Enter marks of subject 1: "))
    s2 = float(input("Enter marks of subject 2: "))
    s3 = float(input("Enter marks of subject 3: "))
    s4 = float(input("Enter marks of subject 4: "))
    s5 = float(input("Enter marks of subject 5: "))
    total = s1 + s2 + s3 + s4 + s5
    average = total / 5
    return total, average

total, average = sum_avg()
print("Total marks: ", total)
print("Average: ", average)  
