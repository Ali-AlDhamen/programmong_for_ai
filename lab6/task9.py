# Task 9: Next Prime 
# In this exercise you will create a function named nextPrime that finds and returns the first prime number larger than some integer, n. The value of n will be passed to the function as its only parameter. Include a main program that reads an integer from the user and displays the first prime number larger than the entered value. Import and use your solution to Task 8 while completing this exercise. 


from task8 import is_prime


def next_prime(n):
    n += 1
    while True:
        if is_prime(n):
            return n
        else:
            n += 1
            

n = int(input("Enter a number: "))
print(f"Next prime number is {next_prime(n)}")