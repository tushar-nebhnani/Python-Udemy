"""
    STUDENT MARKS ANALYZER
    Program Conditions:
    1. Program should allow multiple input for different students, in the format of (name + marks).
    2. Present highest, lowest, average marks.
"""

def collect_student_data():
    students = {}

    while True:
        name = input("Enter the Student Name or 'done' to exist: ").strip()

        if name.lower() == "done":
            break 
        if name in students:
            print("Student alrady exists.")
            continue

        try:
            marks = float(input(f"Enter marks of {name}: "))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks.")

    return students

def display_report(students):
    if not students:
        print("❌ No student data")
        return
    
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    avg_score = sum(marks) / len(marks)


    topper = [name for name, score in students.items() if score == max_score]
    bottomer = [name for name, score in students.items() if score == min_score]

    print("\n*** Students Marks Report ***")
    print(f"Total Students: {len(students)}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Highest marks: {max_score} by {', '. join(topper)}")
    print(f"Lowest marks: {min_score} by {', '. join(bottomer)}")

    print("-" * 30)
    print("Detailed Marks: ")
    for name, score in students.items():
        print(f"- {name}: {score}")
    print("-" * 30)


students = collect_student_data()
display_report(students)