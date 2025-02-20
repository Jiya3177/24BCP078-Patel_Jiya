# Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.

d = {
    101 : [(1, 50000),(2,25000),(3,30000)],
    102 : [(1, 60000),(2, 70000),(3,80000)],
    103 : [(1,50000),(2,90000),(3,80000)]
}
def max_min_salary(self):
    for dept,employees in self.items():
        salary = [salary for _ ,salary in employees]
        max_salary = max(salary)
        min_salary = min(salary)
        print(f"Department {dept} has max salary {max_salary} and min salary {min_salary}")

max_min_salary(d)