# Student Record and Academic Management System

## 1. Introduction

The Student Record and Academic Management System is a menu-driven command-line application developed in Python. It helps a user maintain student identity details, contact information, departments, subjects, marks, attendance, and student clubs.

The program demonstrates core Python concepts such as lists, tuples, dictionaries, sets, functions, loops, conditional statements, exception handling, and input validation.

## 2. Problem Statement

Managing student details manually can make it difficult to search records, update information, calculate academic averages, and prepare basic reports. This project provides a simple command-line system to perform these tasks in one place.

## 3. Objectives

- Add, search, update, delete, and display student records.
- Store subject-wise marks and attendance.
- Calculate a student's total and average marks.
- Identify the student with the highest average marks.
- List students by department and count student records.
- Display unique departments, subjects, and student clubs.
- Validate important inputs and handle invalid numeric entries.
- Demonstrate practical use of Python built-in data structures.

## 4. Scope

The current version is a single-user, command-line application. Records are kept in memory while the program is running. It does not currently use a database or save records to a file.

## 5. Functional Requirements

1. **Add Student:** Collect roll number, registration number, date of birth, name, department, address, email, subjects, marks, attendance, and optional clubs.
2. **Search Student:** Find and display a record using its roll number.
3. **Update Student:** Update name, department, address, email, subjects and marks, or attendance.
4. **Delete Student:** Display a record and ask for confirmation before removing it.
5. **Display All Records:** Show all student records currently in memory.
6. **Calculate Average Marks:** Calculate total marks and average marks for a selected student.
7. **Find Highest Scorer:** Compare students' average marks and display the highest scorer.
8. **List by Department:** Display students whose department matches the entered department, ignoring letter case.
9. **Count Students:** Display the number of records currently stored.
10. **Generate Reports:** Show academic summaries and unique departments, subjects, and clubs.

## 6. Non-Functional Requirements

- The program should be easy to operate through numbered menus.
- Invalid numeric input should be handled without an immediate program crash.
- Marks and attendance should remain between 0 and 100.
- Student roll numbers should be unique within the current in-memory records.
- The code should be divided into functions for readability and reuse.

## 7. Data Structures Used

| Data structure | Use in the project | Reason |
|---|---|---|
| List: `students` | Stores all student dictionaries | Supports adding, iterating through, and removing records |
| Dictionary: `student` | Stores each student's fields | Associates named keys with student details |
| Tuple: `identity` | Stores roll number, registration number, and date of birth | Groups identity fields together |
| Lists: `subjects`, `marks`, `attendance` | Store corresponding subject-wise information | Preserve order and allow multiple entries |
| Set: `departments` | Stores department names encountered during addition or update | Maintains unique values |
| Set: `subjects_set` | Stores subject names encountered during addition or update | Maintains unique values |
| Set: `student_clubs` | Stores club names encountered during student addition | Maintains unique values |

### Example record structure

```python
student = {
    "identity": (101, "REG-101", "2007-01-15"),
    "name": "Example Student",
    "department": "Computer Science",
    "address": "Example address",
    "email": "student@example.com",
    "subjects": ["Mathematics", "Python"],
    "marks": [85.0, 92.0],
    "attendance": [90.0, 95.0],
    "clubs": {"Coding Club"}
}
```

The values above are illustrative examples only.

## 8. Algorithm Descriptions

### Algorithm 1: Add Student
1. Ask the user for a positive roll number.
2. Search existing records for that roll number.
3. If it already exists, show an error and stop this operation.
4. Collect the student's identity and personal details using non-empty input validation.
5. Ask for the number of subjects.
6. For each subject, collect the subject name, marks, and attendance; validate marks and attendance.
7. Collect optional club names and add non-empty names to a set.
8. Create the student dictionary and append it to `students`.
9. Add the department to `departments` and report success.

### Algorithm 2: Search Student
1. Ask for a positive roll number.
2. Call `find_student(roll_number)`.
3. If a matching record is returned, display it.
4. Otherwise, display “Student record not found.”

### Algorithm 3: Update Student
1. Ask for a roll number and find the matching record.
2. If no record exists, display a message and return.
3. Display the update menu.
4. Read the selected option and collect validated replacement values.
5. Update the selected field(s).
6. Repeat until the user selects Back.

### Algorithm 4: Delete Student
1. Ask for a roll number and find the record.
2. If no record exists, display a not-found message.
3. Display the selected student's profile.
4. Ask the user to confirm deletion.
5. Remove the dictionary from `students` only when the answer is `y`.
6. Otherwise, cancel deletion.

### Algorithm 5: Calculate Average Marks
1. Find the student by roll number.
2. If the student is not found, stop and display a message.
3. Retrieve the marks list.
4. If the list is empty, report that marks are unavailable.
5. Calculate `total = sum(marks)`.
6. Calculate `average = total / len(marks)`.
7. Display the total and average.

### Algorithm 6: Find Highest Scorer
1. Check whether any student records exist.
2. Create a list of students whose marks lists are not empty.
3. If that list is empty, report that no marks are available.
4. Calculate the first eligible student's average as the current highest.
5. Compare the average of each eligible student with the current highest.
6. Replace the highest student when a larger average is found.
7. Display the highest scorer's details and average.

### Algorithm 7: List Students by Department
1. Ask for a department name.
2. Set a flag `found` to `False`.
3. Traverse every student record.
4. Compare department names using lowercase versions.
5. Display the roll number and name of each match, and set `found` to `True`.
6. If no match was found, display a not-found message.

## 9. Pseudocode

### Main Menu

```text
START
REPEAT
    DISPLAY main menu
    READ choice

    IF choice = 1, call Add Student
    ELSE IF choice = 2, call Search Student
    ELSE IF choice = 3, call Update Student
    ELSE IF choice = 4, call Delete Student
    ELSE IF choice = 5, call Display All Records
    ELSE IF choice = 6, call Calculate Average
    ELSE IF choice = 7, call Find Highest Scorer
    ELSE IF choice = 8, call List by Department
    ELSE IF choice = 9, call Count Students
    ELSE IF choice = 10, call Generate Reports
    ELSE IF choice = 11, display exit message
    ELSE display invalid-choice message
UNTIL choice = 11
STOP
```

### Calculate Average

```text
START
READ roll number
FIND student using roll number

IF student does not exist
    DISPLAY not-found message
    STOP this operation
END IF

GET student's marks

IF marks list is empty
    DISPLAY no-marks message
    STOP this operation
END IF

total = SUM of marks
average = total / number of marks
DISPLAY total and average
END
```

## 10. Input Validation and Error Handling

The program uses helper functions to validate user input:

- `get_non_empty(prompt)`: repeats until the user enters non-empty text.
- `get_positive_integer(prompt)`: accepts only integers greater than zero and catches `ValueError`.
- `get_mark(prompt)`: accepts numeric marks from 0 through 100.
- `get_attendance(prompt)`: accepts numeric attendance from 0 through 100.
- `find_student(roll_number)`: returns a matching record or `None`.

These functions reduce repeated validation code and make the program easier to maintain.

## 11. Limitations and Future Enhancements

### Current limitations
- Records are held only in memory and disappear when the program exits.
- Registration numbers, email addresses, and dates of birth are only checked for non-empty input; their formats are not validated.
- The update option for subjects and marks does not update attendance at the same time; attendance has a separate menu option.
- The sets of departments, subjects, and clubs are not rebuilt after record deletion. As a result, these sets can contain values no longer used by any current student.
- Subject names are not checked for duplicates within a student's subject list.
- The program is not designed for multiple users or concurrent access.

### Future enhancements
- Add persistent storage using JSON, CSV, or SQLite.
- Validate email, registration number, and date-of-birth formats.
- Recalculate unique departments, subjects, and clubs from current student records.
- Add a grade calculation and attendance eligibility report.
- Add login and role-based access.
- Develop a graphical user interface or web application.
- Add automated unit tests.

## 12. Conclusion

The Student Record and Academic Management System applies fundamental Python programming concepts to a practical record-management problem. It supports common student-record operations and basic academic reporting through a command-line interface. Future improvements such as persistent storage, stronger validation, and automated testing could make it more robust.

## 13. How to Run

1. Install Python 3.8 or later.
2. Open a terminal in the project directory.
3. Run the Python source file. For example:

```bash
python3 student_management.py
```

Replace the filename with the actual name of the Python file in the repository.
