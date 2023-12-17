# Task 1
# Write a program to sort the students’ names and spilt it into two groups each group has 5 students.
# Sample Output:
# group 1: ['Eman' 'Haya' 'Lama' 'Maha' 'Mona']
# group 2: ['Noha' 'Reem' 'Renad' 'Sara' 'Waad']


import numpy as np

students = np.array(['Maha', 'Haya', 'Lama', 'Mona', 'Eman', 'Noha', 'Reem', 'Renad', 'Sara', 'Waad'])
students.sort()
print("Sorted students' names:", students)
np.random.shuffle(students)
print('group 1:', students[:5])
print('group 2:', students[5:])
