

print("Task 1")
A = ["red", "olive", "cyan", "lilac", "mustard"]
print(A[-2])
 



print("Task 2")
A = ["red", "olive", "cyan", "lilac", "mustard"]
print(A[2:])




print("Task 3")
A = ["red", "olive", "cyan", "lilac", "mustard"]
A[1] = "teal"
print(A)




print("Task 4")
A = ["red", "olive", "cyan", "lilac", "mustard"]
B = A[:]
print(B)





print("Task 5")
A = ["red", "olive", "cyan", "lilac", "mustard"]
A.remove("red")
A.remove("lilac")
print(A)

print("Task 6")
X = ("pies", "cake", "bread", "scone", "cookies")
print(X[-3])


print("Task 7")
X = ("pies", "cake", "bread", "scone", "cookies")
print(X[-2:-4:-1])




print("Task 8")
X = ("pies", "cake", "bread", "scone", "cookies")
Y = list(X)
Y[4] = "tart"
X = tuple(Y)
print(X)


print("Task 9")
X = ("pies", "cake", "cookies")
Y = (2, 12, 22)
Z = X + Y
print(Z)



print("Task 10")
Veg = {"pies", "cake", "bread", "scone", "cookies"}
Veg.add("tart")
Veg.add("custard")
Veg.add("waffles")
print(Veg)



print("Task 11")
Veg = {"pies", "cake", "bread", "scone", "cookies"}
Veg.remove("cookies")
print(Veg)



print("Task 12")
Veg = {"pies", "cake", "bread", "scone", "cookies"}
Veg2 = {"tart", "eggos", "custard", "waffles"}
Veg3 = Veg.union(Veg2)
print(Veg3)




print("Task 13")
Hortons = {"type":"cappuccino", "size":"grande", "price":"4.99"}
Hortons["syrup"] = "hazelnut"
print(Hortons)

 


print("Task 14")
Hortons = {"type":"cappuccino", "size":"grande", "price":"4.99"}
Hortons.popitem()
print(Hortons)


print("Task 15")
Hortons = {
    "Coffee01":{
        "name":"cappuccino",
        "size":"venti"
    },
    "Coffee02":{
        "name":"frappe",
        "size":"grande"
    },
    "Coffee03":{
        "name":"macchiato",
        "size":"small"
    }
}
print(Hortons)


print("Task 16")
Hortons = dict(type="cappuccino", size="grande", price="4.99")
print(Hortons)




