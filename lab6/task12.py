# Task 12: Random Good Password 
# Using your solutions to Tasks 10 and 11, write a program that generates a random good password and displays it. Count and display the number of attempts that were needed before a good password was generated. Structure your solution so that it imports the functions you wrote previously and then calls them from a function named main in the file that you create for this exercise. 

from task10 import random_password
from task11 import check_password


def main():
    attempts = 0
    while True:
        attempts += 1
        password = random_password()
        if check_password(password):
            print(f"Password is {password}")
            print(f"Number of attempts: {attempts}")
            break
    
if __name__ == "__main__":
    main()