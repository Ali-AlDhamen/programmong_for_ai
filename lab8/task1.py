import tkinter as tk
import random


def check_guess():
    try:
        user_guess = int(guess_entry.get())
        if user_guess == random_number:
            result_label.config(text="You win!")
        elif user_guess < random_number:
            result_label.config(text="Too low!")
        else:
            result_label.config(text="Too high!")
    except ValueError:
        result_label.config(text="Please enter a valid integer.")
    finally:
        guess_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Guessing Game")


random_number = random.randint(0, 10)

title_label = tk.Label(root, text="Guess a number between 0 and 10", borderwidth=2, relief="solid" )
title_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()


submit_button = tk.Button(root, text="Submit Guess", command=check_guess)
submit_button.pack()


result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()
