"""A small console-based student management system."""

import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    """Load student records from the JSON data file."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            students = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as error:
        raise ValueError(f"{DATA_FILE.name} contains invalid JSON.") from error

    if not isinstance(students, list):
        raise ValueError(f"{DATA_FILE.name} must contain a list of students.")

    for student in students:
        if (
            not isinstance(student, dict)
            or not isinstance(student.get("id"), int)
            or isinstance(student.get("id"), bool)
            or not isinstance(student.get("name"), str)
            or not isinstance(student.get("age"), int)
            or isinstance(student.get("age"), bool)
            or not isinstance(student.get("course"), str)
        ):
            raise ValueError(f"{DATA_FILE.name} contains an invalid student record.")

    return students


def save_students(students):
    """Save student records and report file errors without hiding them."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=2)
            file.write("\n")
    except OSError as error:
        print(f"Could not save student records: {error}")
        return False
    return True


def read_integer(prompt, minimum=0):
    """Read an integer no smaller than the given minimum."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if value < minimum:
            print(f"Please enter a number that is at least {minimum}.")
            continue
        return value


def read_required_text(prompt):
    """Read non-empty text from the console."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def show_students(students):
    if not students:
        print("\nNo student records found.")
        return

    print("\n{:<6} {:<24} {:<8} {}".format("ID", "NAME", "AGE", "COURSE"))
    print("-" * 58)
    for student in students:
        print(
            "{:<6} {:<24} {:<8} {}".format(
                student["id"],
                student["name"][:24],
                student["age"],
                student["course"],
            )
        )


def add_student(students):
    student = {
        "id": max((record["id"] for record in students), default=0) + 1,
        "name": read_required_text("Student name: "),
        "age": read_integer("Age: ", minimum=1),
        "course": read_required_text("Course: "),
    }
    updated_students = students + [student]
    if save_students(updated_students):
        print(f"Student added with ID {student['id']}.")
        return updated_students
    return students


def search_students(students):
    query = input("Enter a student ID or name: ").strip()
    if not query:
        print("Please enter an ID or name to search.")
        return

    if query.isdigit():
        matches = [student for student in students if student["id"] == int(query)]
    else:
        matches = [
            student for student in students if query.casefold() in student["name"].casefold()
        ]
    show_students(matches)


def update_student(students):
    student_id = read_integer("Enter the student ID to update: ", minimum=1)
    index = next(
        (i for i, student in enumerate(students) if student["id"] == student_id),
        None,
    )
    if index is None:
        print("Student not found.")
        return students

    current = students[index]
    print("Press Enter to keep the current value.")
    name = input(f"Name [{current['name']}]: ").strip() or current["name"]
    age_text = input(f"Age [{current['age']}]: ").strip()
    course = input(f"Course [{current['course']}]: ").strip() or current["course"]

    while age_text:
        try:
            age = int(age_text)
            if age < 1:
                raise ValueError
            break
        except ValueError:
            age_text = input("Enter a positive whole number for age: ").strip()
    if not age_text:
        age = current["age"]

    updated_students = [dict(student) for student in students]
    updated_students[index] = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
    }
    if save_students(updated_students):
        print("Student record updated.")
        return updated_students
    return students


def delete_student(students):
    student_id = read_integer("Enter the student ID to delete: ", minimum=1)
    student = next((item for item in students if item["id"] == student_id), None)
    if student is None:
        print("Student not found.")
        return students

    confirm = input(f"Delete {student['name']}? (y/n): ").strip().casefold()
    if confirm != "y":
        print("Deletion cancelled.")
        return students

    updated_students = [item for item in students if item["id"] != student_id]
    if save_students(updated_students):
        print("Student record deleted.")
        return updated_students
    return students


def main():
    try:
        students = load_students()
    except (OSError, ValueError) as error:
        print(f"Could not load student records: {error}")
        return

    while True:
        print(
            "\n=== Student Management System ===\n"
            "1. Add student\n"
            "2. View all students\n"
            "3. Search students\n"
            "4. Update student\n"
            "5. Delete student\n"
            "0. Exit"
        )
        choice = input("Choose an option: ").strip()

        if choice == "1":
            students = add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            students = update_student(students)
        elif choice == "5":
            students = delete_student(students)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 0-5.")


if __name__ == "__main__":
    main()