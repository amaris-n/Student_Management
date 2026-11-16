
def calculate_average(scores):
    """Calculate average score."""
    return sum(scores) / len(scores)


def get_highest_score(scores):
    """Get highest score."""
    return max(scores)


def get_lowest_score(scores):
    """Get lowest score."""
    return min(scores)


def process_students(student_list):
    """Display student names."""
    print("Students:")

    for name in student_list:
        print(name)

    print("Total Students:", len(student_list))


def register_students(*students):
    """Register students."""
    print("Registered Students:")

    for name in students:
        print(name)

    print("Total:", len(students))


if __name__ == "__main__":
    students = ["Ali", "Leyla", "Kamran", "Aysel"]
    scores = [78, 91, 85, 67, 95, 88]

    print("Average Score:", calculate_average(scores))
    print("Highest Score:", get_highest_score(scores))
    print("Lowest Score:", get_lowest_score(scores))

    print()

    process_students(students)

    print()

    register_students("Ali", "Leyla", "Kamran")
