import tkinter as tk
from tkinter import ttk


def submit_ticket():
    name = entry_name.get()
    destination = combo_destination.get()
    flight_time = flight_time_var.get()
    drinks = ', '.join([drink for drink, var in drinks_vars.items() if var.get()])

    ticket_info = f"Your ticket:\nName: {name}\nDestination: {destination}\n" \
                  f"Flight Time: {flight_time}\nDrinks: {drinks}"

    label_ticket_info.config(text=ticket_info, fg='green')


root = tk.Tk()
root.title("New Ticket")


label_name = tk.Label(root, text="Name")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()


label_destination = tk.Label(root, text="Destination")
label_destination.pack()
combo_destination = ttk.Combobox(root, values=["Kuwait", "New York", "London", "Tokyo"])
combo_destination.pack()


flight_time_var = tk.StringVar()
label_flight_time = tk.Label(root, text="Preferred flight time")
label_flight_time.pack()
radio_morning = tk.Radiobutton(root, text="Morning", variable=flight_time_var, value="Morning")
radio_morning.pack()
radio_evening = tk.Radiobutton(root, text="Evening", variable=flight_time_var, value="Evening")
radio_evening.pack()


label_drinks = tk.Label(root, text="Preferred drinks on the plane:")
label_drinks.pack()
drinks_vars = {
    "coffee": tk.BooleanVar(),
    "tea": tk.BooleanVar(),
    "water": tk.BooleanVar()
}
check_coffee = tk.Checkbutton(root, text="Coffee", variable=drinks_vars["coffee"])
check_coffee.pack()
check_tea = tk.Checkbutton(root, text="Tea", variable=drinks_vars["tea"])
check_tea.pack()
check_water = tk.Checkbutton(root, text="Water", variable=drinks_vars["water"])
check_water.pack()


submit_button = tk.Button(root, text="Submit", command=submit_ticket)
submit_button.pack()


label_ticket_info = tk.Label(root, text="", font=('Helvetica', 12), justify=tk.LEFT)
label_ticket_info.pack()


root.mainloop()
