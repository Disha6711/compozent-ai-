class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # List of grades

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


student1 = Student("Disha Gareja", 20, [85, 90, 78, 92])

student1.display_details()

average_grade = student1.calculate_average()
print(f"Average Grade: {average_grade:.2f}")

