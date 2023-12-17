# Task 13: Reduce a Fraction to Lowest Terms 
# Write a function that takes two positive integers that represent the numerator and denominator of a fraction as its only two parameters. The body of the function should reduce the fraction to lowest terms and then return both the numerator and denominator of the reduced fraction as its result. For example, if the parameters passed to the function are 6 and 63 then the function should return 2 and 21. Include a main program that allows the user to enter a numerator and denominator. Then your program should display the re


def reduce_fraction(numerator, denominator):
    for i in range(min(numerator, denominator),1, -1):
        if numerator % i == 0 and denominator % i == 0:
            numerator = numerator // i
            denominator = denominator // i
    return numerator, denominator

print(reduce_fraction(6, 63))
print(reduce_fraction(2, 4))
print(reduce_fraction(5, 10))
print(reduce_fraction(3, 7))
print(reduce_fraction(8, 12))