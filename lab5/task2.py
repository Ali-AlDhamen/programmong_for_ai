# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

animal_crackers = lambda s: s.split()[0][0] == s.split()[1][0]

print(animal_crackers('Levelheaded Llama'))  # True
print(animal_crackers('Crazy Kangaroo'))  # False
