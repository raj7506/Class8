from tkinter import *
from datetime import date
def calculate_age():
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    current_year = date.today().year
    age = current_year - year
    result_label.config(text="You are " + str(age) + " years old.")

root = Tk()

root.geometry("400x400")
root.title("Age Calculator App")
root.config(bg="lightblue")

# Day
Label(root, text="Enter Day", bg="lightblue").pack()

day_entry = Entry(root)
day_entry.pack()

# Month
Label(root, text="Enter Month", bg="lightblue").pack()

month_entry = Entry(root)
month_entry.pack()

# Year
Label(root, text="Enter Year", bg="lightblue").pack()

year_entry = Entry(root)
year_entry.pack()

# Button
Button(root,
       text="Calculate Age",
       command=calculate_age).pack(pady=20)

# Result label
result_label = Label(root,
                     text="",
                     bg="lightblue",
                     font=("Arial", 12, "bold"))

result_label.pack()

# Run window
root.mainloop()