students = []

departments = set()
subjects_set = set()
student_clubs = set()

def get_non_empty(prompt):
    """Get a non-empty string from the user."""

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_integer(prompt):
    """Get a positive integer from the user."""

    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value

            print("Please enter a positive integer.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_mark(prompt):
    """Get marks between 0 and 100."""

    while True:
        try:
            mark = float(input(prompt))

            if 0 <= mark <= 100:
                return mark

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid marks. Please enter a number.")


def get_attendance(prompt):
    """Get attendance between 0 and 100."""

    while True:
        try:
            attendance = float(input(prompt))

            if 0 <= attendance <= 100:
                return attendance

            print("Attendance must be between 0 and 100.")

        except ValueError:
            print("Invalid attendance. Please enter a number.")

def find_student(roll_number):
    """Find a student using roll number."""

    for student in students:

        if student["identity"][0] == roll_number:
            return student

    return None

def display_student(student):
    """Display complete student information."""

    identity = student["identity"]

    print("\n")
    print("=" * 50)
    print("              STUDENT PROFILE")
    print("=" * 50)

    print("Roll Number       :", identity[0])
    print("Registration No.  :", identity[1])
    print("Date of Birth     :", identity[2])

    print("Name              :", student["name"])
    print("Department        :", student["department"])

    print("Address           :", student["address"])
    print("Email             :", student["email"])

    print("Subjects          :", ", ".join(student["subjects"]))

    print("Marks             :", student["marks"])

    print("Attendance        :", student["attendance"])

    if student["clubs"]:
        print("Student Clubs     :", ", ".join(student["clubs"]))
    else:
        print("Student Clubs     : None")

    print("=" * 50)

def add_student():
    """Add a new student record."""

    print("\n")
    print("=" * 50)
    print("                 ADD STUDENT")
    print("=" * 50)

    # Roll number
    roll_number = get_positive_integer(
        "Enter Roll Number: "
    )

    # Duplicate record checking
    if find_student(roll_number) is not None:

        print("\nERROR: Student with this Roll Number already exists.")

        return

    # Student information
    registration_number = get_non_empty(
        "Enter Registration Number: "
    )

    date_of_birth = get_non_empty(
        "Enter Date of Birth: "
    )

    name = get_non_empty(
        "Enter Student Name: "
    )

    department = get_non_empty(
        "Enter Department: "
    )

    address = get_non_empty(
        "Enter Address: "
    )

    email = get_non_empty(
        "Enter Email ID: "
    )
    number_of_subjects = get_positive_integer(
        "Enter Number of Subjects: "
    )

    subject_list = []
    marks_list = []
    attendance_list = []

    for i in range(number_of_subjects):

        print(f"\n--- Subject {i + 1} ---")

        subject = get_non_empty(
            "Enter Subject Name: "
        )

        mark = get_mark(
            f"Enter Marks for {subject}: "
        )

        attendance = get_attendance(
            f"Enter Attendance % for {subject}: "
        )

        # Add to lists
        subject_list.append(subject)

        marks_list.append(mark)

        attendance_list.append(attendance)

        # Add subject to set
        subjects_set.add(subject)

    club_input = input(
        "\nEnter Student Clubs separated by commas "
        "(or press Enter for none): "
    ).strip()

    clubs = set()

    if club_input:

        club_values = club_input.split(",")

        for club in club_values:

            club = club.strip()

            if club:
                clubs.add(club)

                student_clubs.add(club)

    student = {

        # Tuple
        "identity": (
            roll_number,
            registration_number,
            date_of_birth
        ),

        # Strings
        "name": name,

        "department": department,

        "address": address,

        "email": email,

        # Lists
        "subjects": subject_list,

        "marks": marks_list,

        "attendance": attendance_list,

        # Set
        "clubs": clubs
    }

    # Add student dictionary to main list
    students.append(student)

    # Add department to set
    departments.add(department)

    print("\nStudent record added successfully!")

def search_student():
    """Search student using roll number."""

    print("\n")
    print("=" * 50)
    print("               SEARCH STUDENT")
    print("=" * 50)

    roll_number = get_positive_integer(
        "Enter Roll Number: "
    )

    student = find_student(roll_number)

    if student is not None:

        display_student(student)

    else:

        print("\nStudent record not found.")

def update_student():
    """Update student information."""

    print("\n")
    print("=" * 50)
    print("               UPDATE RECORD")
    print("=" * 50)

    roll_number = get_positive_integer(
        "Enter Roll Number: "
    )

    student = find_student(roll_number)

    if student is None:

        print("\nStudent record not found.")

        return

    while True:

        print("""
----------------------------------------
          UPDATE OPTIONS
----------------------------------------

1. Update Name
2. Update Department
3. Update Address
4. Update Email
5. Update Subjects and Marks
6. Update Attendance
7. Back
""")

        choice = input(
            "Enter your choice: "
        ).strip()
        if choice == "1":

            student["name"] = get_non_empty(
                "Enter New Name: "
            )

            print("Name updated successfully.")
        elif choice == "2":

            new_department = get_non_empty(
                "Enter New Department: "
            )

            student["department"] = new_department

            departments.add(new_department)

            print("Department updated successfully.")
        elif choice == "3":

            student["address"] = get_non_empty(
                "Enter New Address: "
            )

            print("Address updated successfully.")

        elif choice == "4":

            student["email"] = get_non_empty(
                "Enter New Email: "
            )

            print("Email updated successfully.")

        elif choice == "5":

            number_of_subjects = get_positive_integer(
                "Enter New Number of Subjects: "
            )

            new_subjects = []
            new_marks = []

            for i in range(number_of_subjects):

                print(f"\n--- Subject {i + 1} ---")

                subject = get_non_empty(
                    "Enter Subject Name: "
                )

                mark = get_mark(
                    f"Enter Marks for {subject}: "
                )

                new_subjects.append(subject)

                new_marks.append(mark)

                subjects_set.add(subject)

            student["subjects"] = new_subjects

            student["marks"] = new_marks

            print("Subjects and marks updated successfully.")

        elif choice == "6":

            new_attendance = []

            for subject in student["subjects"]:

                attendance = get_attendance(
                    f"Enter Attendance for {subject}: "
                )

                new_attendance.append(attendance)

            student["attendance"] = new_attendance

            print("Attendance updated successfully.")

        elif choice == "7":

            break

        else:

            print("Invalid choice. Please try again.")

def delete_student():
    """Delete a student record."""

    print("\n")
    print("=" * 50)
    print("               DELETE RECORD")
    print("=" * 50)

    roll_number = get_positive_integer(
        "Enter Roll Number: "
    )

    student = find_student(roll_number)

    if student is None:

        print("\nStudent record not found.")

        return

    display_student(student)

    confirmation = input(
        "\nAre you sure you want to delete this record? (y/n): "
    ).lower()

    if confirmation == "y":

        students.remove(student)

        print("\nStudent record deleted successfully.")

    else:

        print("\nDeletion cancelled.")

def display_records():
    """Display all student records."""

    print("\n")
    print("=" * 50)
    print("             ALL STUDENT RECORDS")
    print("=" * 50)

    if len(students) == 0:

        print("\nNo student records available.")

        return

    print(
        "\nTotal Records:",
        len(students)
    )

    for student in students:

        display_student(student)

def calculate_average():
    """Calculate average marks of a student."""

    print("\n")
    print("=" * 50)
    print("             CALCULATE AVERAGE")
    print("=" * 50)

    roll_number = get_positive_integer(
        "Enter Roll Number: "
    )

    student = find_student(roll_number)

    if student is None:

        print("\nStudent record not found.")

        return

    marks = student["marks"]

    if len(marks) == 0:

        print("\nNo marks available.")

        return

    total = sum(marks)

    average = total / len(marks)

    print("\nStudent Name :", student["name"])

    print("Total Marks  :", total)

    print(
        "Average Marks:",
        f"{average:.2f}"
    )

def find_highest_scorer():
    """Find student with highest average marks."""

    print("\n")
    print("=" * 50)
    print("              HIGHEST SCORER")
    print("=" * 50)

    if len(students) == 0:

        print("\nNo student records available.")

        return

    students_with_marks = []

    for student in students:

        if len(student["marks"]) > 0:

            students_with_marks.append(student)

    if len(students_with_marks) == 0:

        print("\nNo marks available.")

        return

    highest_student = students_with_marks[0]

    highest_average = (
        sum(highest_student["marks"])
        /
        len(highest_student["marks"])
    )

    for student in students_with_marks:

        average = (
            sum(student["marks"])
            /
            len(student["marks"])
        )

        if average > highest_average:

            highest_average = average

            highest_student = student

    print("\nHighest Scorer")

    print(
        "Name          :",
        highest_student["name"]
    )

    print(
        "Roll Number   :",
        highest_student["identity"][0]
    )

    print(
        "Department    :",
        highest_student["department"]
    )

    print(
        "Average Marks :",
        f"{highest_average:.2f}"
    )
def list_by_department():
    """Display students belonging to a department."""

    print("\n")
    print("=" * 50)
    print("          STUDENTS BY DEPARTMENT")
    print("=" * 50)

    department = get_non_empty(
        "Enter Department: "
    )

    found = False

    print(
        f"\nStudents in Department: {department}"
    )

    print("-" * 50)

    for student in students:

        if (
            student["department"].lower()
            ==
            department.lower()
        ):

            print(
                "Roll Number:",
                student["identity"][0]
            )

            print(
                "Name:",
                student["name"]
            )

            print()

            found = True

    if not found:

        print(
            "No students found in this department."
        )

def count_students():
    """Count total students."""

    print("\n")
    print("=" * 50)
    print("               STUDENT COUNT")
    print("=" * 50)

    total_students = len(students)

    print(
        "\nTotal Number of Students:",
        total_students
    )


def generate_reports():
    """Generate different reports."""

    while True:

        print("""
================================================
                 REPORT MENU
================================================

1. Calculate Average Marks
2. Find Highest Scorer
3. List Students by Department
4. Count Students
5. Show Unique Departments
6. Show Unique Subjects
7. Show Student Clubs
8. Display All Records
9. Back to Main Menu

================================================
""")

        choice = input(
            "Enter your choice: "
        ).strip()

        # Calculate average
        if choice == "1":

            calculate_average()

        # Highest scorer
        elif choice == "2":

            find_highest_scorer()

        # Department
        elif choice == "3":

            list_by_department()

        # Count
        elif choice == "4":

            count_students()

        # Departments set
        elif choice == "5":

            print("\nUnique Departments:")

            if departments:

                for department in departments:

                    print("-", department)

            else:

                print("No departments available.")

        # Subjects set
        elif choice == "6":

            print("\nUnique Subjects:")

            if subjects_set:

                for subject in subjects_set:

                    print("-", subject)

            else:

                print("No subjects available.")

        # Clubs set
        elif choice == "7":

            print("\nStudent Clubs:")

            if student_clubs:

                for club in student_clubs:

                    print("-", club)

            else:

                print("No student clubs available.")

        # All records
        elif choice == "8":

            display_records()

        # Back
        elif choice == "9":

            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )

def main():
    """Main program."""

    while True:

        print("\n")

        print("=" * 60)

        print(
            "       STUDENT RECORD AND ACADEMIC MANAGEMENT SYSTEM"
        )

        print("=" * 60)

        print("""
1.  Add Student
2.  Search Student
3.  Update Student Record
4.  Delete Student Record
5.  Display All Records
6.  Calculate Average Marks
7.  Find Highest Scorer
8.  List Students by Department
9.  Count Students
10. Generate Reports
11. Exit
""")

        print("=" * 60)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            search_student()

        elif choice == "3":

            update_student()

        elif choice == "4":

            delete_student()

        elif choice == "5":

            display_records()

        elif choice == "6":

            calculate_average()

        elif choice == "7":

            find_highest_scorer()

        elif choice == "8":

            list_by_department()

        elif choice == "9":

            count_students()

        elif choice == "10":

            generate_reports()

        elif choice == "11":

            print("\nThank you for using the system!")

            break

        else:

            print(
                "\nInvalid choice. Please enter 1-11."
            )

if __name__ == "__main__":

    main()
