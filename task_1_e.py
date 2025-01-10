class Student:
    # Constructor to initialize student attributes
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # List of grades

    # Method to display student details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    # Method to calculate the average grade
    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


# Example usage
# Create a student object
student1 = Student("Aakanksha", 20, [85, 90, 78, 92])

# Display student details
student1.display_details()

# Calculate and display the average grade
average_grade = student1.calculate_average()
print(f"Average Grade: {average_grade:.2f}")

