# Task 5
# To practice, write a function that adds two matrices together using list comprehensions. The function should take in two 2D lists of the same dimensions. Try to implement this in one line!
# def add_matrices(x, y):
#    "*** YOUR CODE HERE ***"

#     >>> add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]])
#     [[-2, 3], [3, 2]]


def add_matrices(x, y):
    return [[x[i][j]+y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
            
            
print(add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]]))