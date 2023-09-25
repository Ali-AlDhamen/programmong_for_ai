list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)):
    list1.insert(i, list1.pop())

print(list1)
print("Done")