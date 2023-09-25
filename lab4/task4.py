sample_data = input("Enter a string: ")
letters = 0
digits = 0
for i in sample_data:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print("Letters: ", letters)
print("Digits: ", digits)
