# Declare Empty Dictionary
students = {}

# Add data
for i in range(5):
  name = input("Enter student name: ")
  grade = input("Enter grade: ")
  students[name] = grade

# Print Students & Grades
print("\nAll Students & Grades:")

for student in students:
    print(student, ":", students[student])

# Update grade
check_name = input("\nEnter name to update grade: ")

if check_name in students:
    new_grade = input("Enter new grade: ")
    students[check_name] = new_grade
    print("\nGrade updated")
else:
    print("\nStudent not found")

# Print Students & Grades Again
print("\nAll Students & Grades:")

for student in students:
    print(student, ":", students[student])