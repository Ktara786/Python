def get_student_data():
    students = []
    num = int(input("Enter number of students: "))
    for _ in range(num):
        name = input("Enter student name: ")
        marks = float(input(f"Enter marks for {name}: "))
        students.append({"name": name, "marks": marks})
    return students

def analyze_data(students):
    total = 0
    highest = students[0]["marks"]
    lowest = students[0]["marks"]
    toppers = []

    for s in students:
        total += s["marks"]
        if s["marks"] > highest:
            highest = s["marks"]
        if s["marks"] < lowest:
            lowest = s["marks"]

    for s in students:
        if s["marks"] == highest:
            toppers.append(s["name"])

    avg = total / len(students)
    return avg, highest, lowest, toppers

def display_results(students, avg, highest, lowest, toppers):
    print("\n--- Results ---")
    for s in students:
        status = "Pass" if s["marks"] >= 40 else "Fail"
        print(f"{s['name']}: {s['marks']} - {status}")

    print(f"\nAverage Marks: {avg:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print("Topper(s):", ", ".join(toppers))


students = get_student_data()
avg, high, low, toppers = analyze_data(students)
display_results(students, avg, high, low, toppers)
