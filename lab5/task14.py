# Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters. Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the function’s result. Include a main program that reads the lengths of the shorter sides of a right triangle from the user, uses your function to compute the length of the hypotenuse and displays the result. 

def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

a = float(input('Enter the length of the first side: '))
b = float(input('Enter the length of the second side: '))
print('The length of the hypotenuse is', hypotenuse(a, b))