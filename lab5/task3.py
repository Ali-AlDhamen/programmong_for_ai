# Task 3
# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False


def make_twenty(n1,n2):
    return sum([n1,n2]) == 20 or n1 == 20 or n2 == 20

print(make_twenty(20,10)) # True
print(make_twenty(12,8))  # True
print(make_twenty(2,3))   # False