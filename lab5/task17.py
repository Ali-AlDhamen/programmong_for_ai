# Task 17: Median of Three Values 
# Write a function that takes three numbers as parameters and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median. 
# Hint: The median value is the middle of the three values when they are sorted into ascending order. It can be found using if statements, or with a little bit of mathematical creativity. 


median = lambda a,b,c : sorted([a,b,c])[1]

a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
c = float(input('Enter the third number: '))
print('The median is', median(a,b,c))