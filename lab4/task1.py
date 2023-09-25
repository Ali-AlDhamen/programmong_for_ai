numbers = list(map(int , input("Enter numbers: ").split()))
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
        
print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)