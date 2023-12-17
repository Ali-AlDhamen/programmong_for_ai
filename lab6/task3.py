# Task 3
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()


def up_low(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print(f"No. of Upper case characters : {upper}")
    print(f"No. of Lower case characters : {lower}")
    
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
# No. of Upper case characters : 4
# No. of Lower case characters : 33