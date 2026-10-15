# Testing Report

## 1. Purpose

This document describes manual test cases for the Student Record and Academic Management System. Run each test against the current Python program and record the actual result. Do not mark a test as passed until it has been executed.

## 2. Test Environment

- Application: Student Record and Academic Management System
- Language: Python 3
- Interface: Command-line terminal
- External dependencies: None

## 3. Test Cases

| ID | Feature | Test input / action | Expected result | Actual result / status |
|---|---|---|---|---|
| TC-01 | Main menu | Start the program | Main menu appears | To be recorded |
| TC-02 | Add student | Enter valid student details and at least one subject | Record is added successfully | To be recorded |
| TC-03 | Empty required input | Leave a required text field empty | Program asks again for non-empty input | To be recorded |
| TC-04 | Roll number validation | Enter text instead of an integer | Program displays an invalid-input message and asks again | To be recorded |
| TC-05 | Positive integer validation | Enter 0 or a negative roll number | Program asks for a positive integer | To be recorded |
| TC-06 | Duplicate roll number | Add a student using an existing roll number | Duplicate-record error appears; no second record is added | To be recorded |
| TC-07 | Marks lower bound | Enter marks of 0 | Value is accepted | To be recorded |
| TC-08 | Marks upper bound | Enter marks of 100 | Value is accepted | To be recorded |
| TC-09 | Marks out of range | Enter -1 or 101 for marks | Program rejects the value and asks again | To be recorded |
| TC-10 | Attendance out of range | Enter -1 or 101 for attendance | Program rejects the value and asks again | To be recorded |
| TC-11 | Search existing student | Enter a registered roll number | Correct student profile is displayed | To be recorded |
| TC-12 | Search missing student | Enter a roll number not in the list | Not-found message appears | To be recorded |
| TC-13 | Update name | Choose update name and enter a new name | Name changes in the current record | To be recorded |
| TC-14 | Update department | Change a student's department | Department field changes | To be recorded |
| TC-15 | Update subjects and marks | Enter a new subject list and valid marks | Subject and marks lists are replaced | To be recorded |
| TC-16 | Update attendance | Enter attendance for each current subject | Attendance list is replaced | To be recorded |
| TC-17 | Delete cancellation | Select a student and answer `n` | Record remains in the list | To be recorded |
| TC-18 | Delete confirmation | Select a student and answer `y` | Record is removed from the in-memory list | To be recorded |
| TC-19 | Calculate average | Marks are 80 and 90 | Total is 170 and average is 85.00 | To be recorded |
| TC-20 | Highest scorer | Add at least two students with different averages | Student with the highest average is displayed | To be recorded |
| TC-21 | Department search | Search using a department name with different letter casing | Matching students are listed | To be recorded |
| TC-22 | Count students | Add two records and select count | Total is 2 | To be recorded |
| TC-23 | Empty records | Start fresh and display all records | No-records message appears | To be recorded |
| TC-24 | Report menu | Open reports and select unique departments, subjects, and clubs | Available set values are displayed | To be recorded |
| TC-25 | Invalid menu option | Enter an unsupported menu choice | Invalid-choice message appears | To be recorded |
| TC-26 | Exit | Select the exit option | Thank-you message appears and program ends | To be recorded |

## 4. Example Calculation

For marks `[80, 90]`:

- Total = 80 + 90 = 170
- Number of subjects = 2
- Average = 170 / 2 = 85.00

The displayed average should be `85.00`.

## 5. Known Behaviors to Verify

These are limitations in the current implementation, not necessarily failed tests:

1. Records are stored in memory only and are lost after program exit.
2. Updating a student's department adds the new department to the `departments` set but does not remove the old value.
3. Deleting a student does not remove old department, subject, or club names from their global sets.
4. Updating subjects and marks leaves attendance unchanged until the attendance update option is used. If the subject count changes, the attendance list can temporarily have a different length from the subjects list.
5. Club names are added to the global club set when students are added, but clubs are not updated through the update menu.

## 6. Test Summary

After executing the test cases, update this section with the real results.

- Total test cases executed: ___
- Passed: ___
- Failed: ___
- Not executed: ___
- Issues found: ___

## 7. Conclusion

Manual testing should confirm the program's core record-management operations, numeric validation, report calculations, and handling of missing records. Record the actual output for each test before submitting this report.
