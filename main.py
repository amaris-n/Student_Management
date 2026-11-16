
from student_utils import calculate_average
from student_utils import get_highest_score
from student_utils import get_lowest_score
from student_utils import process_students
from student_utils import register_students


students = ["Ali", "Leyla", "Kamran", "Aysel"]
scores = [78, 91, 85, 67, 95, 88]


print("Average Score:", calculate_average(scores))
print("Highest Score:", get_highest_score(scores))
print("Lowest Score:", get_lowest_score(scores))

print()

process_students(students)

print()

register_students("Ali", "Leyla", "Kamran")
