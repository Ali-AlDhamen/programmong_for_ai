# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.



def count_primes(num):
    primes = []
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return len(primes)

print(count_primes(100))  # 25
print(count_primes(0))  # 0
print(count_primes(10))  # 4