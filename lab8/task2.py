import tkinter as tk


def perform_operation(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == 'ADD':
            result = num1 + num2
        elif operation == 'SUB':
            result = num1 - num2
        elif operation == 'MUL':
            result = num1 * num2
        elif operation == 'DIV':
            result = num1 / num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")     
    except ZeroDivisionError:
        label_result.config(text="Cannot divide by zero.")


root = tk.Tk()
root.title("Calculator")


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)


calculator_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Calculator", menu=calculator_menu)


calculator_menu.add_command(label="ADD", command=lambda: perform_operation('ADD'))
calculator_menu.add_command(label="SUB", command=lambda: perform_operation('SUB'))
calculator_menu.add_command(label="MUL", command=lambda: perform_operation('MUL'))
calculator_menu.add_command(label="DIV", command=lambda: perform_operation('DIV'))


entry_num1 = tk.Entry(root)
entry_num1.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()


label_result = tk.Label(root, text="Result: ")
label_result.pack()


root.mainloop()
