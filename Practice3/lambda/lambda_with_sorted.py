students = [("Ali", 85), ("Dana", 92), ("Asyl", 78)]

# Sort by grade
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(sorted_by_grade)

# Sort by name
sorted_by_name = sorted(students, key=lambda student: student[0])
print(sorted_by_name)

# Sort descending by grade
sorted_desc = sorted(students, key=lambda student: student[1], reverse=True)
print(sorted_desc)

# Sort by name length
sorted_length = sorted(students, key=lambda student: len(student[0]))
print(sorted_length)