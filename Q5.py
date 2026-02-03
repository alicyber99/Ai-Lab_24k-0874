class Student:
    def __init__(self, name):
        self.name = name
        self.grade = 0 

    def setGrade(self, grade):
        if 0 <= grade <= 100:
            self.grade = grade
        else:
            print("Invalid grade. Grades 0-100.")

    def getGrade(self):
        return self.grade

    def displayInfo(self):
        print("Name:", self.name)
        print("Grade:", self.grade)
        print()

students = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    grade = int(input("Enter grade (0-100): "))
    s = Student(name)
    s.setGrade(grade)         
    students.append(s)
    print()

for s in students:
    s.displayInfo()           
