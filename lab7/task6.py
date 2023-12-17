# Task 6
# write a list comprehension that will create a deck of cards. Each element in the list will be a card, which is represented by a list containing the suit as a string and the value as an int.
# def deck():
#     "*** YOUR CODE HERE ***"

# Python also includes a powerful sorted function which returns a sorted version of a list. It can also take a key function that tells sorted how to actually sort the objects. For more information, look at Python's documentation for the sorted method. Note that sorted is stable, meaning if two values are equal according to the key function, their relative positions will stay the same after sorting. Now, use the sorted function to write a function that takes in a shuffled deck and returns a sorted deck. It should sort cards of the same suit together, and then sort each card in each suit in increasing value.
# def sort_deck(deck):
#     "*** YOUR CODE HERE ***"

def deck():
    return [[s, v] for s in ['Spades', 'Clubs', 'Hearts', 'Diamonds'] for v in range(1, 14)]

def sort_deck(deck):
    return sorted(deck, key=lambda x: x[1])

dk = deck()
print(sort_deck(dk))


