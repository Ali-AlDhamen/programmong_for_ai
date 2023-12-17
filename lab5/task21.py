# Task 21: Capitalize It
# Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase “i” should be replaced with an uppercase “I” if it is both preceded and followed by a space. The first character in the string should also be capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the function is provided with the string “what time do i have to be there? what’s the address?” then it should return the string “What time do I have to be there? What’s the address?”. Include a main program that reads
# a string from the user, capitalizes it using your function, and displays the result.


capitalize = lambda string: string[0].upper() + ''.join([string[i].upper() if string[i-1] in ['.', '!', '?', ' '] else string[i] for i in range(1, len(string))])

string = input('Enter a string: ')
print(capitalize(string))


