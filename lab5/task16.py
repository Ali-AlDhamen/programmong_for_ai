# Task 16: Shipping Calculator
# An online retailer provides express shipping for many of its items at a rate of $10.95 for the first item, and $2.95 for each subsequent item. Write a function that takes the number of items in the order as its only parameter. Return the shipping charge for the order as the function’s result. Include a main program that reads the number of
# items purchased from the user and displays the shipping charge.


shipping_charge = lambda number_of_items: 10.95 + (number_of_items - 1) * 2.95 if number_of_items > 0 else 0

number_of_items = int(input('Enter the number of items: '))
print(f'The shipping charge is {shipping_charge(number_of_items):.2f}$')
