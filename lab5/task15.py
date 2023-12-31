# Task 15: Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters traveled. Write a function that takes the distance traveled (in kilometers) as its only parameter and returns the total fare as its only result. Write a
# main program that demonstrates the function.

# Hint: Taxi fares change over time. Use constants to represent the base fare and the variable portion of the fare so that the program can be updated easily when the rates increase.


taxi_fare = lambda distance: 4 + (distance * 1000 // 140) * 0.25

distance = float(input('Enter the distance traveled in kilometers: '))
print(f'The total fare is {taxi_fare(distance)}$')
