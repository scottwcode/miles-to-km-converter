# miles-to-km-converter
# This program converts miles to kilometers
# It takes miles as input from the user and when the user clicks
# the calculate button, converts the miles entered into km and
# displays the results
#
from tkinter import *


def calculate_button_clicked():
    """ When Calculate button is clicked convert miles to km and display results """
    miles = float(miles_input.get())
    km = miles * 1.609
    km_output.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# Miles
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Equals
equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)

# Kilometers
km_output = Label(text="0")
km_output.grid(column=1, row=1)
km_after_label = Label(text="Km")
km_after_label.grid(column=2, row=1)

# Calculate Button
button = Button(text="Calculate", command=calculate_button_clicked)
button.grid(column=1, row=2)

window.mainloop()
