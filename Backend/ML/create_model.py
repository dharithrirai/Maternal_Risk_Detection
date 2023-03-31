class Employee:
    def __init__(self, empid, salary):
        self.empid = empid
        self.salary = salary

    def Level(self):
        if self.salary > 1000:
            return 1
        else:
            return 2

    def __str__(self):
        return str(self.empid) + "\n" + str(self.salary) + "\n" + str(self.Level())


class EmpLevel(Employee):
    def __init__(self, empid, salary):
        super().__init__(empid, salary)


emp_input = input().split()
empid = int(emp_input[0])
salary = float(emp_input[1])
emp = EmpLevel(empid, salary)
print(emp)
