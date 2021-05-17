# Tashwill Andries
# importing everything from tkinter
from tkinter import *

root = Tk()
root.title("Temperature converter")
root.config(bg="purple")
root.geometry("700x600")


# creating the first frame
frame = Frame(root, width=300, height=200, highlightbackground="black", highlightthickness=1, bg="grey")
frame.place(x=50, y=51)
celsius_header = Label(frame, text="Celsius to Fahrenheit", bg="grey")
celsius_header.place(x=60, y=0)
celsius_entry = Entry(frame, state="readonly")
celsius_entry.place(x=60, y=150)

# creating the second frame
frame_2 = Frame(root, width=300, height=200, highlightbackground="black", highlightthickness=1, bg="grey")
frame_2.place(x=380, y=51)
fahrenheit_header = Label(frame_2, text="Fahrenheit to Celsius", bg="grey")
fahrenheit_header.place(x=60, y=0)
fahrenheit_entry = Entry(frame_2, state="readonly")
fahrenheit_entry.place(x=60, y=150)

# activate button
def activate_celsius():
    celsius_entry.config(state="normal")
    fahrenheit_entry.config(state="readonly")
    frame.config(bg="white")
    frame_2.config(bg="grey")
    return


# celsius button
Celsius_button = Button(root, text="Activate - Celsius to Fahrenheit", command=activate_celsius)
Celsius_button.place(x=80, y=280)

# fahrenheit activate button
def activate_fehrenheit():
    fahrenheit_entry.config(state="normal")
    celsius_entry.config(state="readonly")
    frame.config(bg="grey")
    frame_2.config(bg="white")

    return


# fahrenheit button
Fahrenheit_button = Button(root, text="Activate - Fahrenheit to Celsius", command=activate_fehrenheit)
Fahrenheit_button.place(x=420, y=280)

# converting to fahrenheit/celsius
def convert():
    if fahrenheit_entry.get() == "":
        celsius = float(celsius_entry.get())
        celsius_convert = (celsius * (9/5) + 32)
        Conversion_answer.config(text=round(celsius_convert))
    elif celsius_entry.get() == "":
        fahrenheit = float(fahrenheit_entry.get())
        fahrenheit_to_celsius = (fahrenheit - 32) * 5/9
        Conversion_answer.config(text=round(fahrenheit_to_celsius))



# conversion
Conversion = Button(root, text="Calculate conversion", command=convert)
Conversion.place(x=90, y=400)
Conversion_answer = Label(root, width=20, height=2, bg="orange")
Conversion_answer.place(x=300, y=400)


def delete():
    celsius_entry.delete(0, END)
    fahrenheit_entry.delete(0, END)
    Conversion_answer.config(text="")


def kill():
    root.destroy()


# clear and Exit button
clear = Button(root, text="Clear", width=15, command=delete)
clear.place(x=500, y=400)
Exit = Button(root, text="exit", width=15, command=kill)
Exit.place(x=500, y=440)

root.mainloop()

