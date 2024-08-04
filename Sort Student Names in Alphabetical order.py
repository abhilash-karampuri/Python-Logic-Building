#A student Register containing student Names and their respective marks. Arrange the student names in alphabetical order.
student_register = {
    'John': 85,
    'Alice': 90,
    'Bob': 75,
    'Diana': 88,
    'Charlie': 92,
    'Chaplin':65
}
sorted_names = sorted(student_register.keys())
print("Student names in alphabetical order with their marks:")
for name in sorted_names:
    print(f"{name}: {student_register[name]}")