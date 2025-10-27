""" 
Unit_Conversion.py

Just a small python script for learning purpose,
This script uses the tkinter which is a package in
the standard Python Liberary.

Author: https://github.com/Mohammaddev54/Mohammaddev54

Date: 2025/10/26

bugs:
- Unintended behaviour when converting from large unit to small unit
- UnImplemented Temperature conversion
-
"""

from tkinter import Tk, ttk, Entry, Button, Label, LabelFrame, Frame, messagebox
# Root Window
root = Tk()
root.title("Units Conversion")
root.resizable(False, False)


def get_info()-> tuple:
    return units_from_list.get(), units_to_list.get(), category_menu_list.get(), user_input_entry.get()


def check_user_input(user_input):
    try:
        user_input_number = int(user_input)
    except ValueError as error:
        return "ERROR"
    return user_input_number


def perform_unit_conversion_on(value_list, unit_1, unit_2, number_entered_by_user):
    """ Formula for converting units of measurement: 
        output = user_input_number  * unit / second unit
        Result is set to output to the nearest 10th decimal place value
    """ 
    unit_names, unit_values = unpack(value_list, 2)
    try:
        from_unit_value =  unit_values[unit_names.index(unit_1)]
        to_unit_value = unit_values[unit_names.index(unit_2)]
        print(to_unit_value)
        print(from_unit_value)
    except ValueError as error1:
        messagebox.showerror("Error!", f"{error1}, You may have two units of different category of measurment")
        return
    result = (number_entered_by_user * from_unit_value) / to_unit_value
    if not 1.0e-10 <= result >= 1.0e10 :
        set_output_value(round(result, 3))
        
    else:
        set_output_value(f"{result:.10e}")


def convert_value():
    from_unit_name, to_unit_name, selected_category, user_input = get_info()
    if selected_category not in categories:
        messagebox.showerror("Error!", "Invalid Catagory!")
        return
    """ 
    BUG: If you choose a unit of measurement like Kilogram and change the Category of units then choose a second unit of measurement like second you can do it but will not return any thing.
        
        Should be fixable.
    """
    if (user_input_number := check_user_input(user_input)) != "ERROR":
        if selected_category == "Length":
            perform_unit_conversion_on(length_units, from_unit_name, to_unit_name, user_input_number)
        elif selected_category == "Mass":
            perform_unit_conversion_on(mass_units, from_unit_name, to_unit_name, user_input_number)
        elif selected_category == "Time":
            perform_unit_conversion_on(time_units, from_unit_name, to_unit_name, user_input_number)
        elif selected_category == "Temperature":
            # No Operations here yet
            set_output_value("Not Implemented")
            raise NotImplementedError
    else:
        set_output_value("ERROR")


def set_output_value(value):
    resulting_output_units_label.config(text=value)

# unpacks the units list from tuple unit_values and unit_names
def unpack(parameter_list, which):
    unit_names, unit_values = zip(*parameter_list)
    if which == 0:
        return unit_names
    elif which == 1:
        return unit_values
    else:
        return unit_names, unit_values


def update_unit_list(from_or_to:int, arg_values):
    if from_or_to == 0:
        units_from_list.config(values=arg_values)
    elif from_or_to == 1:
            units_to_list.config(values=arg_values)
    elif from_or_to == 2:
            units_from_list.config(values=arg_values)
            units_to_list.config(values=arg_values)
    else:
        pass


def set_units_option_list():
    value = category_menu_list.get()
    match value:
        case "Length":
            update_unit_list(2, unpack(length_units, 0))
        case "Mass":
            update_unit_list(2, unpack(mass_units, 0))
        case "Time":
            update_unit_list(2, unpack(time_units, 0))
        case "Temperature":
            # Not Implemented completely
            units_from_list.config(values=temperature_units)
            units_to_list.config(values=temperature_units)
        case _:
            units_from_list.config(values=None)
            units_to_list.config(values=None)


# Units of measurment
length_units = [
    ("meter (m)", 1),
    ("kilometer (km)", 1000),
    ("centimeter (cm)", 0.01),
    ("millimeter (mm)", 0.001),
    ("micrometer (µm)", 0.000001),
    ("nanometer (nm)", 1e-9),
    ("mile (mi)", 1609.34),
    ("yard (yd)", 0.9144),
    ("foot (ft)", 0.3048),
    ("inch (in)", 0.0254),
    ("nautical mile (nmi)", 1852),
    ("light-year (ly)", 9.461e+15),
    ("astronomical unit (AU)", 1.496e+11),
    ("parsec (pc)", 3.086e+16),
    ("furlong", 201.168),
    ("cubit", 0.4572),
    ("league", 4828.03)
]

mass_units = [
    ("kilogram (kg)", 1000),
    ("gram (g)", 1),
    ("milligram (mg)", 0.001),
    ("microgram (µg)", 0.000001),
    ("tonne (t)", 1_000_000),
    ("pound (lb)", 453.59237),
    ("ounce (oz)", 28.3495231),
    ("stone (st)", 6350.29318),
    ("slug", 14593.9029),
    ("carat (ct)", 0.2),
    ("grain (gr)", 0.06479891),
    ("hundredweight (cwt)", 50802.34544)  # UK hundredweight
]

time_units = [
    ("second (s)", 1),
    ("millisecond (ms)", 0.001),
    ("microsecond (µs)", 0.000001),
    ("nanosecond (ns)", 1e-9),
    ("minute (min)", 60),
    ("hour (h)", 3600),
    ("day (d)", 86400),
    ("week (wk)", 604800),
    ("fortnight", 1209600),  # 2 weeks
    ("month", 2629800),      # Average month (30.44 days)
    ("year (yr)", 31557600), # Average year (365.25 days)
    ("decade", 315576000),
    ("century", 3155760000),
    ("millennium", 3.15576e10),
    ("shake (10^-8 s)", 1e-8)
]

temperature_units = [
    "Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)", "Rankine (°R)", "Réaumur (°Re)"
]

categories = ["Length", "Mass", "Time", "Temperature"]
all_units = [*length_units, *mass_units, *time_units, *temperature_units]
# Frames
main_frame = Frame(root, bg="#FFFFFF")
main_frame.pack()
master_window = main_frame

measuring_category_label_frame = LabelFrame(master=master_window, text="Catagory")
measuring_category_label_frame.columnconfigure(weight=1, index=2)
measuring_category_label_frame.pack(ipadx=10, ipady=10, padx=10, pady=10)

units_from_label_frame = LabelFrame(master_window, text="From")
units_from_label_frame.pack(ipadx=10, ipady=10, padx=10, pady=10)

convert_to_label_frame = LabelFrame(master_window, text="Convert To")
convert_to_label_frame.pack(ipadx=10, ipady=10, padx=10, pady=10)

# Menu Lists
category_menu_list = ttk.Combobox(measuring_category_label_frame, values=categories)
category_menu_list.grid(row=2, column=0, padx=5, pady=5)

units_from_list = ttk.Combobox(units_from_label_frame)
units_from_list.bind("<Button-1>", lambda event: set_units_option_list())
units_from_list.grid(row=0, column=0, padx=5, pady=5)

units_to_list = ttk.Combobox(convert_to_label_frame)
units_to_list.bind("<Button-1>", lambda event: set_units_option_list())
units_to_list.grid(row=1, column=0, padx=5, pady=5)

# Entries
user_input_entry = Entry(units_from_label_frame)
user_input_entry.grid(row=0, column=1, padx=5, pady=5)

# Output Labels
resulting_output_units_label = Label(convert_to_label_frame, bg="#F4F4F4", bd=1, relief="sunken", width=15)
resulting_output_units_label.grid(row=1, column=1, padx=5, pady=5)

# Buttons
convert_button = Button(master_window, text="Convert", command=convert_value)
convert_button.pack()

root.mainloop()
