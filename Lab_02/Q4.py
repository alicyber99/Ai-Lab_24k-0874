class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        print("Manager is planning and managing the team.\n")

class Developer(Employee):
    def work(self):
        print("Developer is writing and testing code.\n")

class Designer(Employee):
    def work(self):
        print("Designer is creating UI/UX designs.\n")

e1 = Manager()
e2 = Developer()
e3 = Designer()
employees = [e1, e2, e3]

print("Employee Management System\n")
for emp in employees:
    emp.work()
