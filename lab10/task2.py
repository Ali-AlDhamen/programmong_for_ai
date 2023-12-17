# Task 2
# Write program to print the following:
# •	students’ names who got above 90 in the homework. 
# •	Highest grade
# •	Lowest grade
# •	Randomly pick a student name to solve the homework.
# First you should create two arrays :
# Array 1: students’ names
# Array 2: to hold the students' grades.

# Sample Output:
# A+ students are:
# ['Sara' 'Reem']
# highest grade:  99
# lowest grade:  87
# Sara will solve the homework


import numpy as np

students = np.array(['Maha', 'Haya', 'Lama', 'Mona', 'Eman', 'Noha', 'Reem', 'Renad', 'Sara', 'Waad'])
grades = np.random.randint(70, 100, 10)
print('students:', students)
print('grades:', grades)
print('A+ students are:')
print(students[grades > 90])
print('highest grade:', grades.max())
print('lowest grade:', grades.min())
print(np.random.choice(students), 'will solve the homework')
