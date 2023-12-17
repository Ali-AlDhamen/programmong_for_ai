# Task 2

# Using range, write a comprehension whose value is a dictionary. The keys should be the integers from 0 to 99 and the value corresponding to a key should be the square of the key.



squares = {x:x**2 for x in range(1,100)}
print(squares)