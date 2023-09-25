number_of_terms = int(input("Enter the number of terms: "))
result = 0
for i in range(1, number_of_terms + 1):
    result += int(i * "2")
print(result)