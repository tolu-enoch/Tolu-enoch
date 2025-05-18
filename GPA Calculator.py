# gpa_calculator.py

def grade_to_point(grade):
    grade = grade.upper()
    return {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 0
    }.get(grade, -1)  # Return -1 for invalid grades

def compute_gpa():
    courses = {
        'GEC320': 2,
        'GEC321': 2,
        'GEC324': 2,
        'EIE323': 3,
        'EIE326': 3,
        'EIE327': 3
    }

    total_points = 0
    total_units = 0

    print("Enter grades for the following courses (A-F):")

    for course, unit in courses.items():
        while True:
            grade = input(f"{course}: ")
            point = grade_to_point(grade)
            if point == -1:
                print("Invalid grade. Enter a letter between A and F.")
                continue
            total_points += point * unit
            total_units += unit
            break

    gpa = total_points / total_units
    print(f"\nYour GPA is: {gpa:.2f}")

if __name__ == "__main__":
    compute_gpa()
