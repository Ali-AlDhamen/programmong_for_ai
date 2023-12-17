# Task 1

# Write a comprehension over a range of the form range(n) such that the value of the comprehension is the set of odd numbers from 1 to 99.

odd_numbers = [x for x in range(1,100) if x%2!=0]
print(odd_numbers)