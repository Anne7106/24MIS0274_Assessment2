students = {"John": {"Python": 85, "Mathematics": 78, "AI": 92},"Alice": {"Python": 65, "Mathematics": 72, "AI": 68},"Bob": {"Python": 35, "Mathematics": 45, "AI": 30},"David": {"Python": 90, "Mathematics": 88, "AI": 95},"Emma": {"Python": 55, "Mathematics": 48, "AI": 62}}
for name, marks in students.items():
    total = marks["Python"] + marks["Mathematics"] + marks["AI"]
    percentage = total / 3
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    marks["Total"] = total
    marks["Percentage"] = percentage
    marks["Grade"] = grade
print("----- STUDENT RESULTS -----")
for name, marks in students.items():
    print("\nName:", name)
    print("Python:", marks["Python"])
    print("Mathematics:", marks["Mathematics"])
    print("AI:", marks["AI"])
    print("Total:", marks["Total"])
    print("Percentage:", marks["Percentage"])
    print("Grade:", marks["Grade"])
topper = max(students, key=lambda name: students[name]["Percentage"])
print("\n----- CLASS TOPPER -----")
print("Topper:", topper)
print("Percentage:", students[topper]["Percentage"])
print("\n----- STUDENTS WHO FAILED -----")
for name, marks in students.items():
    if (marks["Python"] < 40 or
        marks["Mathematics"] < 40 or
        marks["AI"] < 40):
        print(name)
sorted_students = sorted(students.items(),key=lambda item: item[1]["Percentage"],reverse=True)
print("\n----- STUDENTS SORTED BY PERCENTAGE -----")
for name, marks in sorted_students:
    print(name, "-", marks["Percentage"], "%")
