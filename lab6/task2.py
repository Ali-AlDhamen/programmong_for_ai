# Task 2
# Write a function that checks whether a number is in a given range (inclusive of high and low)


def run_check(num , low , high):
    if num in range(low,high+1):
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is not in the range between {low} and {high}")

def run_bool(num , low , high):
    return num in range(low,high+1)     


run_check(5,2,7)
run_check(3,1,10)
run_check(11,1,10)

print(run_bool(5,2,7))
print(run_bool(3,1,10))
print(run_bool(11,1,10))

