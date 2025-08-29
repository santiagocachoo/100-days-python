from tkinter import *
window = Tk()
window.title("GUI Program")
window.minsize(500, 300)

# label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

def button_click():
    #my_label.config(text="Button got clicked")
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_click)
button.pack()

# Entry
input = Entry(width=10)
input.pack()




window.mainloop()