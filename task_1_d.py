# Initialize an empty dictionary to store student data
students = {}

# Function to create a new student record
def create_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists.")
        return
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    grades = list(map(float, input("Enter Grades (separated by spaces): ").split()))
    students[student_id] = {"name": name, "age": age, "grades": grades}
    print("Student record created successfully.")

# Function to read student data
def read_student():
    student_id = input("Enter Student ID to view details: ")
    if student_id in students:
        print("Student Details:")
        print(f"Name: {students[student_id]['name']}")
        print(f"Age: {students[student_id]['age']}")
        print(f"Grades: {students[student_id]['grades']}")
    else:
        print("Student ID not found.")

# Function to update an existing student record
def update_student():
    student_id = input("Enter Student ID to update: ")
    if student_id in students:
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        grades = list(map(float, input("Enter New Grades (separated by spaces): ").split()))
        students[student_id] = {"name": name, "age": age, "grades": grades}
        print("Student record updated successfully.")
    else:
        print("Student ID not found.")

# Function to delete a student record
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student record deleted successfully.")
    else:
        print("Student ID not found.")

# Menu to perform CRUD operations
def menu():
    while True:
        print("\nStudent Management System")
        print("1. Create Student")
        print("2. Read Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            create_student()
        elif choice == '2':
            read_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()
