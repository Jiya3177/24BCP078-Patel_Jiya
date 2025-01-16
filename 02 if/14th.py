# grade of students Marks Range Grade
# Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail.

subject1 = int(input("Enter marks of subject 1: "))
subject2 = int(input("Enter marks of subject 2: "))
subject3 = int(input("Enter marks of subject 3: "))

def calculate_total(subject1, subject2, subject3):
    print("The total of all subject is", end=(" "))
    print (subject1 + subject2 + subject3)

def calculate_average(subject1, subject2, subject3):
    print("The average of all subject is", end=(" "))
    print ((subject1 + subject2 + subject3)/3)

print("fail") if ( subject1 <= 39 or subject2 <= 39 or subject3 <= 39 ) else print("pass")
def calculate_grade(score):
    if (score >= 80 and score < 100):
        print("grade is O")
    elif (score >= 70 and score < 80):
        print("grade is A+")
    elif (score >= 60 and score < 70):
        print("grade is A")
    elif (score >= 55 and score < 60):
        print("grade is B+")
    elif (score >= 50 and score < 55):
        print("grade is B")
    elif (score >= 45 and score < 50):
        print("grade is C")
    elif (score >= 40 and score < 45):
        print("grade is D")
    elif (score >= 0 and score < 40):
        print("grade is F")
    else:
        print("grade is NA")

calculate_total(subject1, subject2, subject3)
calculate_average(subject1, subject2, subject3)
print("grade of subject1",end=(" "))
calculate_grade(subject1)
print("grade of subject2",end=(" "))
calculate_grade(subject2)
print("grade of subject3",end=(" "))
calculate_grade(subject3)  