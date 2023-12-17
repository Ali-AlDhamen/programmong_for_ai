# Task 11: Check a Password 
# In this exercise you will write a function that determines whether or not a password is good. We will define a good password to be a one that is at least 8 characters long and contains at least one uppercase letter, at least one lowercase letter, and at least one number. Your function should return true if the password passed to it as its only parameter is good. Otherwise it should return false. Include a main program that reads a password from the user and reports whether or not it is good. Ensure that your main program only runs when your solution has not been imported into another file. 


def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    
    for i in password:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True
    
    return len(password) >= 8 and has_upper and has_lower and has_digit

    
def main():
    print(check_password("12345678"))
    print(check_password("aaaaaaaaaaAAAaA"))
    print(check_password("1234567890"))
    print(check_password("123456789Aa1"))
    print(check_password("123456789AaA"))
    

if __name__ == "__main__":
    main()