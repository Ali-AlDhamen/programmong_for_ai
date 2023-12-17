
# Task 18: Convert an Integer to its Ordinal Number
# Words like first, second and third are referred to as ordinal numbers. In this exercise, you will write a function that takes an integer as its only parameter and returns a string containing the appropriate English ordinal number as its only result. Your function must handle the integers between 1 and 12 (inclusive). It should return an empty string if a value outside of this range is provided as a parameter. Include a main program that demonstrates your function by displaying each integer from 1 to 12 and its ordinal number. Your main program should only run when your file has
# not been imported into another program.


def ordinal_number(number):
    match number:
        case 1:
            return 'first'
        case 2:
            return 'second'
        case 3:
            return 'third'
        case 4:
            return 'fourth'
        case 5:
            return 'fifth'
        case 6:
            return 'sixth'
        case 7:
            return 'seventh'
        case 8:
            return 'eighth'
        case 9:
            return 'ninth'
        case 10:
            return 'tenth'
        case 11:
            return 'eleventh'
        case 12:
            return 'twelfth'
        case _:
            return ''
        
for i in range(1, 13):
    print(i, ordinal_number(i))
