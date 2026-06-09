students = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78
}

name = input("Enter student name: ")

if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")