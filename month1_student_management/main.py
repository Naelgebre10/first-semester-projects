# main.py

from student_data import add_student, view_students, get_average_grade

def menu():
    while True:
        print("====== STUDENT MANAGEMENT SYSTEM ======")
        print("1️⃣  Add Student")
        print("2️⃣  View Students")
        print("3️⃣  Calculate Average Grade")
        print("4️⃣  Exit")
        print("=======================================")

        choice = input("Enter your choice (1–4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            get_average_grade()
        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
