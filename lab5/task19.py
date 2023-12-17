# Task 19: Center a String in the Terminal
# Write a function that takes a string of characters as its first parameter, and the width of the terminal in characters as its second parameter. Your function should return a new string that consists of the original string and the correct number of leading spaces so that the original string will appear centered within the provided width when it is printed. Do not add any characters to the end of the string. Include a main program
# that demonstrates your function.


center_string = lambda string, width: ' ' * ((width - len(string)) // 2) + string

string = input('Enter a string: ')
width = int(input('Enter the width of the terminal: '))
print(center_string(string, width))
