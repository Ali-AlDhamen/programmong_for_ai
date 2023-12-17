# Task 3
# Write a program that calculate and classify the rainfall average for 4 weeks.
# 1-	Firstly, create 2D array (4,7)  to store the rainfall rates for each day in the 4 weeks.
# week#1	9	8	6	9	7	6	8
# week#2	2	1	2	3	2	3	5
# week#3	3	5	5	7	3	2	6
# week#4	4	3	5	6	7	3	2

# 2-	Secondly, calculate the average of each week and print it.
import numpy as np

rainfall = np.array([[9, 8, 6, 9, 7, 6, 8], [2, 1, 2, 3, 2, 3, 5], [3, 5, 5, 7, 3, 2, 6], [4, 3, 5, 6, 7, 3, 2]])

for i in range(4):
    average = rainfall[i].mean().round(2)
    print('Week', i + 1, ':')
    if average >= 6:
        print('High:', average)
    elif average > 3:
        print('Medium:', average)
    else:
        print('Low:', average)
        