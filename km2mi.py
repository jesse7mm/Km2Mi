import tkinter as tk

def convert_km_to_miles():
    try:
        km = float(entry.get())
        miles = km * 0.621371
        miles_rounded = round(miles, 1)
        result_label.config(text=f"{km} kilometers = {miles_rounded} miles")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Kilometers to Miles Converter")

# Create input label and entry
input_label = tk.Label(root, text="Enter kilometers:")
input_label.pack()

entry = tk.Entry(root)
entry.pack()

# Create conversion button
convert_button = tk.Button(root, text="Convert", command=convert_km_to_miles)
convert_button.pack()

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
