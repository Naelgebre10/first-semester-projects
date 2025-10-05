# student_data.py

students = []  # A list to hold student dictionaries

def add_student():
    name = input("Enter student name: ").strip()
    try:
        age = int(input("Enter student age: "))
        grade = float(input("Enter student grade (0–100): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for age and grade.\n")
        return

    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print(f"✅ {name} has been added successfully!\n")

def view_students():
    if not students:
        print("⚠️ No students found.\n")
        return

    print("\n📋 Student List:")
    for i, s in enumerate(students, start=1):
        print(f"{i}. Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
    print()

def get_average_grade():
    if not students:
        print("⚠️ No student data to calculate average.\n")
        return

    avg = sum(s["grade"] for s in students) / len(students)
    print(f"📊 The average grade is: {avg:.2f}\n")
