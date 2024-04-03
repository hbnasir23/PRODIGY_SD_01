import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature():
    try:
        value = float(entry.get())
        unit = unit_var.get()
        if unit == "Celsius (°C)":
            celsius = value
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
        elif unit == "Fahrenheit (°F)":
            fahrenheit = value
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = fahrenheit_to_kelvin(fahrenheit)
        elif unit == "Kelvin (K)":
            kelvin = value
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = kelvin_to_fahrenheit(kelvin)

        result_celsius.config(text=f"Celsius: {celsius:.2f}°C")
        result_fahrenheit.config(text=f"Fahrenheit: {fahrenheit:.2f}°F")
        result_kelvin.config(text=f"Kelvin: {kelvin:.2f}K")

        if celsius > 30:
            temp_status = "Too Hot"
        elif celsius > 20:
            temp_status = "Hot"
        elif celsius < 10:
            temp_status = "Too Cold"
        elif celsius < 20:
            temp_status = "Cold"
        else:
            temp_status = "Moderate"

        result_status.config(text=f"Temperature Status: {temp_status}")

    except ValueError:
        result_celsius.config(text="")
        result_fahrenheit.config(text="")
        result_kelvin.config(text="")
        result_status.config(text="")

def update_dropdown_options(*args):
    selected_unit = unit_var.get()
    if selected_unit != "Celsius (°C)":
        unit_options.remove("Celsius (°C)")
        unit_options.append("Celsius (°C)")
    unit_dropdown['menu'].delete(0, 'end')
    for option in unit_options:
        unit_dropdown['menu'].add_command(label=option, command=tk._setit(unit_var, option))

root = tk.Tk()
root.title("Temperature Converter")
root.configure(bg='teal')

style = ttk.Style()
style.configure('TFrame', background='teal')
style.configure('TLabel', background='yellow', font=('Helvetica', 14))

frame = ttk.Frame(root, padding="20", style='TFrame')
frame.grid(row=0, column=0)

instruction_label_temp = ttk.Label(frame, text="Please enter the temperature:", style="TLabel")
instruction_label_temp.grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="ew")

entry = ttk.Entry(frame, font=("Helvetica", 14), width=10)
entry.grid(row=1, column=0, pady=(0, 10), sticky="ew")

instruction_label_unit = ttk.Label(frame, text="Select unit:", style="TLabel")
instruction_label_unit.grid(row=2, column=0, columnspan=3, pady=(0, 10), sticky="ew")

unit_var = tk.StringVar(frame)
unit_var.set("Celsius (°C)")
unit_options = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]

unit_dropdown = ttk.OptionMenu(frame, unit_var, *unit_options)
unit_dropdown.grid(row=3, column=0, pady=(0, 10), sticky="ew")
unit_dropdown.bind("<Configure>", update_dropdown_options)

convert_button = ttk.Button(frame, text="Convert", command=convert_temperature, style="TButton")
convert_button.grid(row=4, column=0, pady=(10, 0), sticky="ew")

result_celsius = ttk.Label(frame, font=("Helvetica", 14), text="", style="TLabel")
result_celsius.grid(row=5, column=0, pady=(10, 0), sticky="ew")

result_fahrenheit = ttk.Label(frame, font=("Helvetica", 14), text="", style="TLabel")
result_fahrenheit.grid(row=6, column=0, pady=(10, 0), sticky="ew")

result_kelvin = ttk.Label(frame, font=("Helvetica", 14), text="", style="TLabel")
result_kelvin.grid(row=7, column=0, pady=(10, 0), sticky="ew")

result_status = ttk.Label(frame, font=("Helvetica", 14), text="", style="TLabel")
result_status.grid(row=8, column=0, pady=(10, 0), sticky="ew")

root.update()
width = frame.winfo_reqwidth()
height = frame.winfo_reqheight()
x_position = (root.winfo_screenwidth() - width) // 2
y_position = (root.winfo_screenheight() - height) // 2
root.geometry(f"{width}x{height}+{x_position}+{y_position}")

root.mainloop()
