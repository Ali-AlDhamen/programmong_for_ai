# Task 3
# What would Python display? Try to figure it out before you type it into the interpreter!

# >>> [x*x for x in range(5)]
# ______

# >>> [n for n in range(10) if n % 2 == 0]
# ______

# >>> ones = [1 for i in ["hi", "bye", "you"]]
# >>> ones + [str(i) for i in [6, 3, 8, 4]]
# ______

# >>> [i+5 for i in [n for n in range(1,4)]]
# ______

# >>> [i**2 for i in range(10) if i < 3]
# ______
# >>> lst = ['hi' for i in [1, 2, 3]]
# >>> print(lst)
# ______
# >>> lst + [i for i in ['1', '2', '3']]


print([x*x for x in range(5)])

print([n for n in range(10) if n % 2 == 0])

ones = [1 for i in ["hi", "bye", "you"]]
print(ones + [str(i) for i in [6, 3, 8, 4]])


print([i+5 for i in [n for n in range(1,4)]])


print([i**2 for i in range(10) if i < 3])


lst = ['hi' for i in [1, 2, 3]]
print(lst)

print(lst + [i for i in ['1', '2', '3']])