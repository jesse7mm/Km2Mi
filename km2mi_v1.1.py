import tkinter as tk

def convert():
    try:
        value = float(entry.get())
        if selected_option.get() == "Kilometers to Miles":
            result = value * 0.621371
            result_rounded = round(result, 1)
            result_label.config(text=f"{value} kilometers = {result_rounded} miles")
        elif selected_option.get() == "Miles to Kilometers":
            result = value * 1.60934
            result_rounded = round(result, 1)
            result_label.config(text=f"{value} miles = {result_rounded} kilometers")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Distance Converter")

# Dropdown for conversion options
options = ["Kilometers to Miles", "Miles to Kilometers"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Default selection

option_menu = tk.OptionMenu(root, selected_option, *options)
option_menu.pack()

# Create input label and entry
input_label = tk.Label(root, text="Enter value:")
input_label.pack()

entry = tk.Entry(root)
entry.pack()

# Create conversion button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
