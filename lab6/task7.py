# Task 7
# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: You may want to use .replace() method to get rid of spaces.
# Hint: Look at the string module
# Hint: In case you want to use set comparisons

import string

def is_pangram(str1, alphabet=string.ascii_lowercase):
    alpha_set = set(alphabet) # has all the letters of the alphabet
    return alpha_set <= set(str1.lower()) # checks if str1 has all the letters of the alphabet aka superset of alpha_set

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))