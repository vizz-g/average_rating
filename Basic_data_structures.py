#Task "Average score":
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
average_rating = {}
for student_name, grade_average in zip(students_sort, grades):
    average_grade = sum(grade_average) / len(grade_average)
    average_rating[student_name] = average_grade

print(average_rating)