from tkinter import *
from tkinter import messagebox

# Universal Properties
universal_font = ('Arial', 20, 'bold')

# Initialise Root i.e Window
root = Tk()


# Labels Are Here
weight_label = Label(root, text="Weight : ", font=universal_font)
weight_label.grid(row=0, column=0)

height_label = Label(root, text="Height : ", font=universal_font)
height_label.grid(row=1, column=0)


def calculate_bmi():
    # Lets get the values from each entry
    wght = weight.get()
    hght = height.get()
    # Notes: BMI - Formula = (weight / height ^ 2)
    bmi = (wght / ((hght**2) / 1000))  # We'r converting it to metre..
    messagebox.showinfo("Results", f"Your BMI is: {bmi}")


# We need Height And Weight Entries
# Text Variables are here...
global weight
global height

weight = IntVar()
height = IntVar()

weight_entry = Entry(root, textvariable=weight, width=40,
                     bd=6, font=universal_font)

weight_entry.grid(row=0, column=1)


height_entry = Entry(root, textvariable=height, width=40,
                     bd=6, font=universal_font)

height_entry.grid(row=1, column=1)

# Now We need A Button...
btn_calculate = Button(root, width=40, text="Calculate",
                       font=universal_font, bd=6, command=calculate_bmi)
btn_calculate.grid(row=2, columnspan=3, pady=10)

# Root Window Configurations...
root.title("BMI Calculator")
root.resizable(False, False)
root.mainloop()
