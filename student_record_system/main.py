"""Command-line Student Record Management System.

Run:
    python main.py
Optional storage format:
    python main.py --format json
    python main.py --format csv
"""
import argparse
from student_manager import StudentManager


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_age():
    while True:
        try:
            age = int(input("Age: ").strip())
            if age <= 0:
                raise ValueError("Age must be a positive integer.")
            return age
        except ValueError as error:
            print(f"Invalid age: {error}")


def get_marks():
    while True:
        try:
            marks = float(input("Marks (0-100): ").strip())
            if not 0 <= marks <= 100:
                raise ValueError("Marks must be between 0 and 100.")
            return marks
        except ValueError as error:
            print(f"Invalid marks: {error}")


def collect_student():
    return {
        "student_id": get_non_empty("Student ID: "),
        "name": get_non_empty("Name: "),
        "age": get_age(),
        "course": get_non_empty("Course: "),
        "marks": get_marks(),
        "email": get_non_empty("Email: "),
    }


def print_students(students):
    if not students:
        print("\nNo student records found.")
        return
    print("\n{:<12} {:<22} {:<6} {:<20} {:<8} {}".format(
        "ID", "NAME", "AGE", "COURSE", "MARKS", "EMAIL"
    ))
    print("-" * 88)
    for student in students:
        print("{:<12} {:<22} {:<6} {:<20} {:<8} {}".format(
            student["student_id"], student["name"][:21], student["age"],
            student["course"][:19], student["marks"], student["email"]
        ))


def main():
    parser = argparse.ArgumentParser(description="Student Record Management System")
    parser.add_argument("--format", choices=["csv", "json"], default="csv",
                        help="Storage format (default: csv)")
    args = parser.parse_args()

    manager = StudentManager(storage_format=args.format)
    print(f"Student Record Management System | Storage: {args.format.upper()}")

    while True:
        print("""
1. Add student
2. View all students
3. Search student by ID
4. Update student
5. Delete student
6. Exit
""")
        choice = input("Choose an option (1-6): ").strip()
        try:
            if choice == "1":
                manager.add_student(collect_student())
                print("Student added successfully.")
            elif choice == "2":
                print_students(manager.get_all_students())
            elif choice == "3":
                student_id = get_non_empty("Enter student ID: ")
                student = manager.get_student(student_id)
                print_students([student] if student else [])
            elif choice == "4":
                student_id = get_non_empty("Enter student ID to update: ")
                existing = manager.get_student(student_id)
                if not existing:
                    print("Student not found.")
                    continue
                print("Enter the new details:")
                updated = collect_student()
                if updated["student_id"] != student_id:
                    print("Student ID cannot be changed during update.")
                    continue
                manager.update_student(student_id, updated)
                print("Student updated successfully.")
            elif choice == "5":
                student_id = get_non_empty("Enter student ID to delete: ")
                if manager.delete_student(student_id):
                    print("Student deleted successfully.")
                else:
                    print("Student not found.")
            elif choice == "6":
                print("Thank you for using the Student Record Management System.")
                break
            else:
                print("Please enter a number from 1 to 6.")
        except (ValueError, OSError) as error:
            print(f"Operation could not be completed: {error}")


if __name__ == "__main__":
    main()
