# Task 3
# find out the execution time of  evenFun function using class decorator.

# •	evenFun(x,y): sum all even numbers from x to y.
# * you can use time.time() that returns the time as a floating point number expressed in seconds since the epoch, in UTC.
import time

class TimeDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        start = time.time()
        ans = self.func(*args)
        end = time.time()
        print(f"Execution time: {end-start} seconds")
        return ans



@TimeDecorator
def evenFun(x, y):
    return sum([i for i in range(x, y+1) if i % 2 == 0])


print(evenFun(1, 1000000))

