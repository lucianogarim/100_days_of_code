from tkinter import *


def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_result_label.config(text=f"{round(km, 2)}")


window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

# Label
miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal", font=("Arial", 16, "bold"))
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=1)

# Entry
miles_input = Entry(width=7)
print(miles_input.get())
miles_input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

km_result_label = Label(text='0', font=("Arial", 16, "bold"))
km_result_label.grid(column=1, row=1)

window.mainloop()