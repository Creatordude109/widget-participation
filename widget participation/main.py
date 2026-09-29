from tkinter import Tk, Label, Entry, Text, Button, END
from datetime import date

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)
name_lbl = Label(text="Enter your name", fg="white", bg="#072F5F", height=1, width=300)
name_entry = Entry()
text_box = Text(height=5, width=50)


def display():
    name = name_entry.get()
    message = "Welcome to the Application!\nToday's date is "
    greet = "Hello, " + name + "!"

    text_box.insert(END, greet + "\n")
    text_box.insert(END, message)
    text_box.insert(END, str(date.today()))


btn = Button(text="Click Me!", command=display, fg="white", bg="#072F5F", height=1, width=300)

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()