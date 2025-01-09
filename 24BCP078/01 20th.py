# Calculate net salary where net salary = gross salary + allowance - deduction.
# Allowances are 10% while deductions are 3% of gross salary. 
salary = float(input("enter salary: "))
allowances = salary * 0.1
deduction = salary * 0.03

net_salary = salary + allowances - deduction
print("net salary is: ", net_salary)  